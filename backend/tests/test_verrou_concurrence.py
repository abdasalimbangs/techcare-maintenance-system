
import threading

from sqlalchemy import func, select

# Utiliser le moteur PostgreSQL réservé aux tests.
from app.database.test_connection import engine_test


def test_deux_connexions_ne_peuvent_pas_obtenir_le_meme_verrou():
    """
    Vérifier qu'une deuxième connexion attend la libération
    du verrou transactionnel détenu par la première connexion.
    """

    # Signaler que la connexion A a obtenu le verrou.
    verrou_obtenu = threading.Event()

    # Autoriser la connexion A à terminer sa transaction.
    autoriser_liberation = threading.Event()

    # Signaler que la connexion B a obtenu le verrou.
    deuxieme_connexion_autorisee = threading.Event()

    # Signaler que la connexion B commence sa tentative.
    tentative_connexion_b = threading.Event()

    # Conserver les éventuelles erreurs survenues dans les threads.
    erreurs = []

    def connexion_a():
        """Obtenir le verrou et le conserver jusqu'à la validation."""

        try:
            # Ouvrir une première connexion PostgreSQL indépendante.
            with engine_test.connect() as connexion:
                transaction = connexion.begin()

                try:
                    # Obtenir le verrou transactionnel identifié par 224007.
                    connexion.execute(
                        select(func.pg_advisory_xact_lock(224007))
                    )

                    # Informer le programme principal que le verrou est obtenu.
                    verrou_obtenu.set()

                    # Attendre l'autorisation de terminer la transaction.
                    if not autoriser_liberation.wait(timeout=10):
                        raise TimeoutError(
                            "La connexion A n'a pas reçu l'autorisation."
                        )

                    # Valider la transaction et libérer le verrou.
                    transaction.commit()

                except Exception:
                    # Annuler la transaction si une erreur survient.
                    if transaction.is_active:
                        transaction.rollback()
                    raise

        except Exception as erreur:
            # Transmettre l'erreur au programme principal.
            erreurs.append(erreur)

    def connexion_b():
        """Essayer d'obtenir le verrou détenu par la connexion A."""

        try:
            # Ouvrir une deuxième connexion PostgreSQL indépendante.
            with engine_test.connect() as connexion:
                transaction = connexion.begin()

                try:
                    # Signaler que la connexion B commence sa tentative.
                    tentative_connexion_b.set()

                    # Cette instruction attend si la connexion A détient encore le verrou.
                    connexion.execute(
                        select(func.pg_advisory_xact_lock(224007))
                    )

                    # Signaler que le verrou est maintenant obtenu.
                    deuxieme_connexion_autorisee.set()

                    # Valider la transaction et libérer le verrou.
                    transaction.commit()

                except Exception:
                    # Annuler la transaction si une erreur survient.
                    if transaction.is_active:
                        transaction.rollback()
                    raise

        except Exception as erreur:
            # Transmettre l'erreur au programme principal.
            erreurs.append(erreur)

    # Préparer les deux fils d'exécution indépendants.
    thread_a = threading.Thread(target=connexion_a)
    thread_b = threading.Thread(target=connexion_b)

    try:
        # Démarrer la première connexion.
        thread_a.start()

        # Attendre que la première connexion obtienne réellement le verrou.
        assert verrou_obtenu.wait(timeout=5), (
            "La connexion A n'a pas obtenu le verrou."
        )

        # Démarrer la deuxième connexion.
        thread_b.start()

        # Attendre que la deuxième connexion commence sa tentative.
        assert tentative_connexion_b.wait(timeout=5), (
            "La connexion B n'a pas commencé sa tentative."
        )

        # Vérifier que B ne peut pas obtenir le verrou pendant que A le détient.
        assert not deuxieme_connexion_autorisee.wait(timeout=0.5), (
            "La connexion B a obtenu le verrou trop tôt."
        )

        # Autoriser A à valider sa transaction et à libérer le verrou.
        autoriser_liberation.set()

        # Vérifier que B obtient le verrou après sa libération.
        assert deuxieme_connexion_autorisee.wait(timeout=5), (
            "La connexion B n'a pas obtenu le verrou après sa libération."
        )

    finally:
        # Éviter de laisser le premier thread bloqué en cas d'échec du test.
        autoriser_liberation.set()

        # Attendre la fin des deux fils d'exécution.
        thread_a.join(timeout=10)
        thread_b.join(timeout=10)

    # Vérifier que les deux threads ont terminé correctement.
    assert not thread_a.is_alive(), "Le thread A ne s'est pas terminé."
    assert not thread_b.is_alive(), "Le thread B ne s'est pas terminé."

    # Faire remonter les éventuelles erreurs survenues dans les threads.
    assert not erreurs, f"Une erreur est survenue : {erreurs}"
