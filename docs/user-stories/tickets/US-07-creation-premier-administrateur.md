# US-07 — Créer le premier compte administrateur

**Type :** User Story
**Priorité :** Haute
**Statut :** À faire

## Description

En tant que responsable de TechCare, je veux créer le premier compte administrateur à l'aide d'un code d'activation afin de sécuriser l'accès à l'administration.

## Objectif métier

Permettre au responsable de créer le compte administrateur initial tout en empêchant toute création ultérieure d'un autre compte administrateur.

## Critères d'acceptation

- [] Une page permet de créer le premier compte administrateur.
- [] Le formulaire demande le nom, le prénom, l'adresse e-mail, le mot de passe et le code d'activation.
- [] Tous ces champs sont obligatoires.
- [] Le système vérifie que le code d'activation est correct.
- [] Le système vérifie qu'aucun compte administrateur n'existe déjà.
- [] Si toutes les vérifications réussissent, le compte est créé.
- [] Après la création, toute nouvelle tentative d'inscription administrateur est refusée.
- [] Si le code est incorrect, le compte n'est pas créé et un message d'erreur est affiché.
- [] Le mot de passe est stocké de manière sécurisée, jamais en clair.

## Règles de sécurité

- Le code d'activation est conservé dans les variables d'environnement du serveur.
- Le code d'activation ne doit jamais être exposé au frontend.
- Le mot de passe doit être haché avant son stockage.
- Les tentatives d'activation doivent être limitées.
- La création du premier administrateur doit être protégée contre les inscriptions concurrentes.

## Périmètre technique

- Frontend : React JavaScript.
- Backend : FastAPI.
- Base de données : PostgreSQL.
- ORM : SQLAlchemy.
- Tests : Pytest.

## Définition de terminé (Definition of Done)

- Tous les critères d'acceptation sont validés.
- Les validations frontend et backend sont réalisées.
- Les règles de sécurité sont testées.
- Les tests automatisés passent.
- Le code est documenté lorsque nécessaire.
- Le commit est réalisé et la branche est fusionnée après revue.
