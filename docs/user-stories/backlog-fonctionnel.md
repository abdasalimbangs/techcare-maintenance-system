# TechCare Mini — Backlog fonctionnel

**Version :** 1.0 — Revue fonctionnelle validée  
**Statut :** Validé  
**Projet :** TechCare Mini

---

## 1. Présentation du projet

TechCare Mini est une mini-marketplace destinée à une entreprise unique. Elle permet de présenter des produits et des services sur une interface publique et de recevoir les demandes des clients.

Un espace d'administration privé permet à l'administrateur de gérer le catalogue et de traiter les demandes reçues.

L'objectif du MVP est de disposer d'une application simple, sécurisée, évolutive et déployable en production.

## 2. Acteurs du système

### 2.1 Visiteur / Client

Le visiteur peut :
- Consulter les produits disponibles.
- Consulter les services disponibles.
- Voir les détails d'un produit ou d'un service.
- Envoyer une demande concernant un produit.
- Envoyer une demande concernant un service.

Le client n'a pas besoin de créer un compte.

### 2.2 Administrateur

L'administrateur peut :
- Créer le premier compte administrateur.
- Se connecter à l'espace d'administration.
- Ajouter, consulter et modifier les produits.
- Désactiver et réactiver les produits.
- Ajouter, consulter et modifier les services.
- Désactiver et réactiver les services.
- Consulter les demandes des clients.
- Consulter les détails des demandes.
- Modifier le statut des demandes selon les règles définies.

Le MVP prévoit un seul compte administrateur.

---

# 3. User Stories et critères d'acceptation

## Bloc 1 — Fonctionnalités du client

### US-01 — Consulter la liste des produits

**User Story**

En tant que visiteur, je veux consulter la liste des produits proposés par TechCare afin de découvrir les produits disponibles.

**Critères d'acceptation**

1. Le visiteur peut accéder à la liste des produits sans créer de compte.
2. Seuls les produits actifs sont affichés.
3. Chaque produit présente au minimum son nom et sa description.
4. Si aucun produit actif n'existe, un message indique qu'aucun produit n'est disponible.
5. Si le chargement échoue, un message informe le visiteur du problème.

### US-02 — Consulter la liste des services

**User Story**

En tant que visiteur, je veux consulter la liste des services proposés par TechCare afin de vérifier s'ils correspondent à mes besoins.

**Critères d'acceptation**

1. Le visiteur peut consulter les services sans créer de compte.
2. Seuls les services actifs sont affichés.
3. Chaque service présente au minimum son nom et sa description.
4. Si aucun service actif n'existe, un message adapté est affiché.
5. En cas d'erreur de chargement, le visiteur est informé.

### US-03 — Consulter les détails d'un produit

**User Story**

En tant que visiteur, je veux consulter les détails d'un produit afin de mieux comprendre ses caractéristiques avant d'envoyer une demande.

**Critères d'acceptation**

1. Le visiteur peut sélectionner un produit dans le catalogue.
2. Le système affiche les informations détaillées du produit.
3. Un produit inactif ne peut pas être consulté publiquement.
4. Si le produit n'existe pas ou n'est plus disponible, un message adapté est affiché.
5. Le visiteur peut revenir à la liste des produits.

### US-04 — Consulter les détails d'un service

**User Story**

En tant que visiteur, je veux consulter les détails d'un service afin de comprendre ce que TechCare propose avant de faire une demande.

**Critères d'acceptation**

1. Le visiteur peut sélectionner un service dans le catalogue.
2. Le système affiche les informations détaillées du service.
3. Un service inactif ne peut pas être consulté publiquement.
4. Si le service n'existe pas ou n'est plus disponible, un message adapté est affiché.
5. Le visiteur peut revenir à la liste des services.

### US-05 — Envoyer une demande concernant un produit

**User Story**

En tant que client, je veux envoyer une demande concernant un produit afin de contacter TechCare pour obtenir des informations ou manifester mon intérêt.

**Critères d'acceptation**

1. Le client peut envoyer une demande sans créer de compte.
2. Le formulaire contient :
   - Nom : obligatoire.
   - Téléphone : obligatoire.
   - Email : facultatif.
   - Message : obligatoire.
3. Le système vérifie que les champs obligatoires sont renseignés.
4. Le système vérifie que le produit est toujours actif au moment de l'enregistrement.
5. Si le produit est inactif, la demande est refusée.
6. Si les informations sont valides, la demande est enregistrée et associée au produit concerné.
7. Le client reçoit une confirmation lorsque sa demande est enregistrée.
8. En cas d'erreur, le client est informé et la demande n'est pas présentée comme envoyée.

### US-06 — Envoyer une demande concernant un service

**User Story**

En tant que client, je veux envoyer une demande concernant un service afin de solliciter une prestation auprès de TechCare.

**Critères d'acceptation**

1. Le client peut envoyer une demande sans créer de compte.
2. Le formulaire contient :
   - Nom : obligatoire.
   - Téléphone : obligatoire.
   - Email : facultatif.
   - Message : obligatoire.
3. Les champs obligatoires doivent être validés.
4. Le système vérifie que le service est toujours actif au moment de l'enregistrement.
5. Si le service est inactif, la demande est refusée.
6. Si les informations sont valides, la demande est enregistrée et associée au service concerné.
7. Le client reçoit une confirmation après l'enregistrement.
8. En cas d'erreur, un message adapté est affiché.

---

## Bloc 2 — Administrateur et gestion des produits

### US-07 — Créer le premier compte administrateur

**User Story**

En tant que responsable de TechCare, je veux créer le premier compte administrateur à l'aide d'un code d'activation afin de sécuriser l'accès à l'administration.

**Critères d'acceptation**

1. Une page permet de créer le premier compte administrateur.
2. Le formulaire demande le nom, l'adresse e-mail, le mot de passe et le code d'activation.
3. Le nom, l'e-mail, le mot de passe et le code sont obligatoires.
4. Le système vérifie que le code d'activation est correct.
5. Le système vérifie qu'aucun compte administrateur n'existe déjà.
6. Si les vérifications réussissent, le compte est créé.
7. Après la création, toute nouvelle tentative d'inscription administrateur est refusée.
8. Si le code est incorrect, le compte n'est pas créé et un message d'erreur est affiché.
9. Le mot de passe est stocké de manière sécurisée, jamais en clair.

### US-08 — Se connecter à l'administration

**User Story**

En tant qu'administrateur, je veux me connecter à mon espace d'administration afin de gérer les produits, les services et les demandes des clients.

**Critères d'acceptation**

1. L'administrateur dispose d'une page de connexion.
2. Il saisit son adresse e-mail et son mot de passe.
3. Si les informations sont correctes, il accède à son espace d'administration.
4. Si les informations sont incorrectes, un message d'erreur est affiché.
5. Un visiteur non authentifié ne peut pas accéder aux pages privées de l'administration.
6. Une fois déconnecté, l'administrateur ne peut plus accéder à son espace privé sans se reconnecter.

### US-09 — Ajouter un produit

**User Story**

En tant qu'administrateur, je veux ajouter un produit afin de le présenter dans le catalogue public de TechCare.

**Critères d'acceptation**

1. L'administrateur peut accéder au formulaire d'ajout d'un produit.
2. Il peut renseigner les informations du produit, notamment son nom et sa description.
3. Les informations obligatoires sont vérifiées avant l'enregistrement.
4. Si les informations sont valides, le produit est enregistré.
5. Le nouveau produit est actif par défaut et peut apparaître dans le catalogue public.
6. En cas d'erreur, un message informe l'administrateur que l'enregistrement a échoué.

### US-10 — Consulter les produits dans l'administration

**User Story**

En tant qu'administrateur, je veux consulter la liste de tous les produits afin de gérer le catalogue de TechCare.

**Critères d'acceptation**

1. L'administrateur peut accéder à la liste des produits.
2. La liste affiche les produits actifs et inactifs.
3. Chaque produit présente au minimum son nom et son statut.
4. L'administrateur peut distinguer les produits actifs des produits inactifs.
5. Si aucun produit n'existe, un message adapté est affiché.
6. En cas d'erreur de chargement, l'administrateur est informé.

### US-11 — Modifier un produit

**User Story**

En tant qu'administrateur, je veux modifier les informations d'un produit afin de maintenir le catalogue à jour.

**Critères d'acceptation**

1. L'administrateur peut sélectionner un produit existant.
2. Le système affiche ses informations actuelles.
3. L'administrateur peut modifier les informations autorisées.
4. Les champs obligatoires sont vérifiés avant l'enregistrement.
5. Si les informations sont valides, les modifications sont enregistrées.
6. Si le produit n'existe plus, un message adapté est affiché.
7. En cas d'erreur, les modifications ne sont pas présentées comme enregistrées.

### US-12 — Désactiver et réactiver un produit

**User Story**

En tant qu'administrateur, je veux désactiver un produit afin de le retirer du catalogue public sans perdre son historique.

**Critères d'acceptation**

1. L'administrateur peut sélectionner un produit actif.
2. Le système lui demande de confirmer la désactivation.
3. Après confirmation, le produit devient inactif.
4. Le produit disparaît du catalogue public.
5. Le produit reste consultable dans l'administration.
6. Les demandes déjà enregistrées concernant ce produit sont conservées.
7. Le produit n'est pas supprimé définitivement de la base de données.
8. L'administrateur peut réactiver un produit précédemment désactivé.
9. Après réactivation, le produit redevient visible dans le catalogue public.
10. Les anciennes demandes liées au produit restent conservées.

---

## Bloc 3 — Gestion des services

### US-13 — Ajouter un service

**User Story**

En tant qu'administrateur, je veux ajouter un service afin de le présenter dans le catalogue public de TechCare.

**Critères d'acceptation**

1. L'administrateur peut accéder au formulaire d'ajout d'un service.
2. Il peut renseigner le nom et la description du service.
3. Les champs obligatoires sont vérifiés.
4. Si les informations sont valides, le service est enregistré.
5. Le service est actif par défaut et peut apparaître dans le catalogue public.
6. L'administrateur peut choisir entre un prix fixe et la mention « Prix sur demande ».
7. Si un prix fixe est choisi, le montant doit être renseigné et valide.
8. Si « Prix sur demande » est choisi, aucun montant fixe n'est exigé.
9. Le catalogue public affiche le prix fixe ou la mention « Prix sur demande », selon le choix de l'administrateur.
10. En cas d'erreur, un message adapté est affiché.

### US-14 — Consulter les services dans l'administration

**User Story**

En tant qu'administrateur, je veux consulter tous les services afin de gérer le catalogue de services de TechCare.

**Critères d'acceptation**

1. L'administrateur peut consulter la liste des services.
2. La liste affiche les services actifs et inactifs.
3. Chaque service présente au minimum son nom et son statut.
4. L'administrateur peut distinguer les services actifs des services inactifs.
5. Si aucun service n'existe, un message adapté est affiché.
6. En cas d'erreur de chargement, l'administrateur est informé.

### US-15 — Modifier un service

**User Story**

En tant qu'administrateur, je veux modifier les informations d'un service afin de maintenir le catalogue à jour.

**Critères d'acceptation**

1. L'administrateur peut sélectionner un service existant.
2. Le système affiche ses informations actuelles.
3. L'administrateur peut modifier les informations autorisées.
4. Il peut choisir entre un prix fixe et « Prix sur demande ».
5. Si un prix fixe est choisi, le montant doit être renseigné et valide.
6. Si « Prix sur demande » est choisi, aucun montant fixe n'est exigé.
7. Les champs obligatoires sont vérifiés avant l'enregistrement.
8. Si les informations sont valides, les modifications sont enregistrées.
9. Si le service n'existe plus, un message adapté est affiché.
10. En cas d'erreur, les modifications ne sont pas présentées comme enregistrées.

### US-16 — Désactiver et réactiver un service

**User Story**

En tant qu'administrateur, je veux désactiver un service afin de le retirer du catalogue public sans perdre son historique.

**Critères d'acceptation**

1. L'administrateur peut sélectionner un service actif.
2. Le système lui demande de confirmer la désactivation.
3. Après confirmation, le service devient inactif.
4. Le service disparaît du catalogue public.
5. Il reste consultable dans l'administration.
6. Les demandes déjà enregistrées concernant ce service sont conservées.
7. Le service n'est pas supprimé définitivement.
8. L'administrateur peut réactiver un service précédemment désactivé.
9. Après réactivation, le service redevient visible publiquement.
10. Les anciennes demandes restent conservées.

---

## Bloc 4 — Gestion des demandes clients

### US-17 — Consulter la liste des demandes

**User Story**

En tant qu'administrateur, je veux consulter toutes les demandes reçues afin de suivre les sollicitations des clients.

**Critères d'acceptation**

1. Seul l'administrateur connecté peut accéder à la liste.
2. Le système affiche les demandes concernant les produits et les services.
3. Chaque demande affiche au minimum :
   - Le nom du client.
   - Son numéro de téléphone.
   - Son adresse e-mail, si renseignée.
   - Le produit ou service concerné.
   - La date de réception.
   - Le statut de la demande.
4. L'administrateur peut distinguer les demandes nouvelles, en cours et traitées.
5. Si aucune demande n'existe, un message adapté est affiché.
6. En cas d'erreur de chargement, l'administrateur est informé.

### US-18 — Consulter les détails d'une demande

**User Story**

En tant qu'administrateur, je veux consulter les détails d'une demande afin de comprendre précisément le besoin du client.

**Critères d'acceptation**

1. L'administrateur peut sélectionner une demande.
2. Le système affiche les coordonnées du client.
3. Le système affiche le message complet du client.
4. Le système affiche le produit ou service concerné.
5. Le système affiche la date de réception et le statut actuel.
6. Si la demande n'existe pas, un message adapté est affiché.

### US-19 — Modifier le statut d'une demande

**User Story**

En tant qu'administrateur, je veux modifier le statut d'une demande afin de suivre son traitement.

**Critères d'acceptation**

1. L'administrateur peut modifier le statut d'une demande.
2. Les statuts disponibles sont :
   - Nouvelle.
   - En cours.
   - Traitée.
3. Le statut initial d'une nouvelle demande est « Nouvelle ».
4. L'administrateur peut faire évoluer le statut vers « En cours » lorsqu'il commence le traitement.
5. L'administrateur peut passer le statut à « Traitée » lorsque le traitement est terminé.
6. Le nouveau statut est enregistré en base de données.
7. Le nouveau statut est visible dans la liste et dans les détails de la demande.
8. En cas d'erreur, le système informe l'administrateur et conserve le statut précédent.
9. Une demande ayant le statut « Traitée » ne peut plus être rouverte ni revenir à un autre statut.

---

# 4. Règles métier

| Référence | Règle métier |
|---|---|
| RM-001 | Seuls les produits et services actifs sont visibles dans le catalogue public. |
| RM-002 | Une demande concernant un produit ou service inactif au moment de l'enregistrement est refusée. |
| RM-003 | Le client peut envoyer une demande sans créer de compte. |
| RM-004 | Le nom, le téléphone et le message sont obligatoires ; l'e-mail est facultatif. |
| RM-005 | Seul l'administrateur authentifié peut accéder à l'administration. |
| RM-006 | Les produits et services sont désactivés plutôt que supprimés définitivement dans le MVP. |
| RM-007 | Les demandes historiques doivent être conservées. |
| RM-008 | Un seul compte administrateur est autorisé dans le MVP. |
| RM-009 | L'administrateur gère le catalogue et toutes les demandes. |
| RM-010 | La création du premier compte administrateur nécessite un code d'activation valide. |
| RM-011 | Après la création du premier compte administrateur, l'inscription initiale est fermée. |
| RM-012 | L'administrateur peut réactiver un produit désactivé sans créer un nouvel enregistrement. |
| RM-013 | L'administrateur peut réactiver un service désactivé sans créer un nouvel enregistrement. |
| RM-014 | Chaque service peut avoir un prix fixe ou être proposé à un prix communiqué sur demande. |
| RM-015 | Une demande traitée est définitive et son statut ne peut plus être modifié. |

---

# 5. Périmètre du MVP

## Fonctionnalités incluses

- Catalogue public de produits.
- Catalogue public de services.
- Consultation des détails.
- Formulaires de demandes clients sans compte.
- Création sécurisée du premier compte administrateur.
- Connexion et déconnexion administrateur.
- Gestion des produits.
- Gestion des services.
- Gestion des statuts des demandes.
- Conservation des données historiques.

## Fonctionnalités exclues du MVP

Les éléments suivants pourront faire l'objet d'évolutions ultérieures :

- Paiement en ligne.
- Gestion des commissions.
- Livraison.
- Multi-vendeurs.
- Application mobile.
- Gestion complexe des stocks.
- Facturation complexe.
- Notifications SMS et WhatsApp.
- Gestion de plusieurs administrateurs.

---

# 6. Choix techniques du projet

| Partie | Technologie |
|---|---|
| Interface utilisateur | React avec JavaScript |
| Backend | Python avec FastAPI |
| Base de données | PostgreSQL |
| Communication | API REST |
| Documentation API | Swagger / OpenAPI |
| Tests backend | Pytest |
| Conteneurisation | Docker |
| Gestion de versions | Git et GitHub |

Le backend constitue la source de vérité pour les règles métier et la sécurité. Le frontend ne doit jamais être considéré comme une protection suffisante.

---

# 7. Points restant à préciser pendant la conception

Ces éléments ne remettent pas en cause la validation fonctionnelle du backlog. Ils devront être décidés avant ou pendant la conception détaillée :

1. Les champs définitifs d'un produit et d'un service.
2. La présence éventuelle d'images et de prix pour les produits.
3. Les formats et règles de validation des numéros de téléphone.
4. Les règles de sécurité détaillées du code d'activation.
5. La politique de mot de passe et la récupération de compte.
6. Les transitions techniques autorisées entre les statuts des demandes, notamment l'interdiction de modifier une demande traitée.
7. Les limites de taille et les validations des messages clients.

---

# 8. État du document

**Revue fonctionnelle : terminée.**

- US-01 à US-06 : validées.
- US-07 à US-12 : validées.
- US-13 à US-16 : validées.
- US-17 à US-19 : validées.

Ce backlog constitue la référence fonctionnelle du MVP TechCare Mini. Toute modification ultérieure devra être identifiée et validée avant d'être intégrée au projet.

## Visualisation des dépendances

Voici comment je vois l'enchaînement général du projet :

### Création administrateur
- US-07

### Authentification
- US-08

### Gestion des produits
- US-10, US-09, US-11, US-12

### Catalogue produits
- US-01, US-03

### Gestion des services
- US-14, US-13, US-15, US-16

### Catalogue services
- US-02, US-04

### Gestion des demandes publiques
- US-05, US-06

### Traitement des demandes par l'administrateur
- US-17, US-18, US-19