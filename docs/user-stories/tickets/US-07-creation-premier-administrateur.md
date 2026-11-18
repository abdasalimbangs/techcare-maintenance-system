# US-07 — Création du premier administrateur

## 1. Description

**En tant que** responsable de TechCare Mini,  
**je veux** créer le premier compte administrateur à l’aide d’un code d’activation,  
**afin de** sécuriser l’accès à l’espace d’administration.

## 2. Informations du formulaire

Le formulaire de création du premier administrateur doit contenir les champs suivants :

- Nom
- Prénom
- Adresse e-mail
- Mot de passe
- Code d’activation

Tous les champs sont obligatoires.

## 3. Critères d’acceptation

- Le formulaire de création du premier administrateur est accessible lorsqu’aucun administrateur n’existe.
- Le système vérifie que tous les champs obligatoires sont renseignés.
- Le système vérifie la validité du code d’activation.
- Le système vérifie qu’aucun compte administrateur n’a déjà été créé.
- Si toutes les vérifications réussissent, le compte administrateur est créé.
- Si le code d’activation est incorrect, aucun compte n’est créé et un message d’erreur est affiché.
- Après la création du premier administrateur, toute nouvelle tentative de création d’un compte administrateur par cette procédure est refusée.

## 4. Règles métier

- Un seul compte administrateur peut être créé par cette procédure.
- Le nom et le prénom sont obligatoires.
- L’adresse e-mail doit être unique.
- Le code d’activation est défini côté serveur.
- Le code d’activation ne doit jamais être stocké dans la base de données.
- Le code d’activation ne doit jamais être exposé dans le frontend.
- Le mot de passe doit être enregistré sous forme de hash.

## 5. Sécurité

- Utiliser une comparaison sécurisée pour vérifier le code d’activation.
- Limiter le nombre de tentatives de saisie du code.
- Ne jamais afficher ni journaliser le mot de passe ou le code d’activation.
- Empêcher deux créations simultanées du premier administrateur.

## 6. Périmètre technique

**Backend :**
- Vérification de l’existence d’un administrateur.
- Validation des données reçues.
- Vérification du code d’activation.
- Hashage du mot de passe.
- Création du compte administrateur.
- Protection contre les créations concurrentes.

**Frontend :**
- Formulaire de création du premier administrateur.
- Validation des champs.
- Affichage des erreurs et du résultat de la création.

**Tests :**
- Création avec des données valides.
- Refus avec un code incorrect.
- Refus si un administrateur existe déjà.
- Vérification du hash du mot de passe.
- Vérification des tentatives répétées et des créations simultanées.

## 7. Définition de terminé (Definition of Done)

- Les critères d’acceptation sont respectés.
- Les règles métier et de sécurité sont appliquées.
- Les tests automatisés passent.
- Le formulaire frontend communique correctement avec le backend.
- Le ticket est documenté et les modifications sont validées par Git.

## 8. Endpoint disponible

- GET /api/administrateurs/inscription-disponible
- POST /api/administrateurs/inscription
