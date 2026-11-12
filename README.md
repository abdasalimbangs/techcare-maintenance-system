# TechCare Mini

## Présentation

TechCare Mini est une mini-marketplace développée pour une entreprise unique. Elle permet de présenter des produits et des services à des visiteurs et de recevoir leurs demandes à travers une interface publique.

L'application dispose également d'un espace d'administration sécurisé permettant de gérer le catalogue et de traiter les demandes des clients.

## Objectifs

- Présenter les produits et services de l'entreprise.
- Permettre aux visiteurs de consulter les informations disponibles.
- Permettre aux clients de contacter l'entreprise sans créer de compte.
- Faciliter la gestion du catalogue.
- Centraliser les demandes reçues.
- Construire une application maintenable, évolutive et déployable en production.

## Acteurs

### Visiteur / Client
- Consulter les produits et services actifs.
- Consulter leurs détails.
- Envoyer une demande concernant un produit.
- Envoyer une demande concernant un service.

Aucun compte client n'est nécessaire.

### Administrateur
- Créer le premier compte administrateur avec un code d'activation.
- Se connecter à l'administration.
- Ajouter, consulter et modifier les produits.
- Désactiver et réactiver les produits.
- Ajouter, consulter et modifier les services.
- Désactiver et réactiver les services.
- Consulter les demandes et leurs détails.
- Suivre le traitement des demandes.

Le MVP prévoit un seul administrateur.

## Fonctionnalités du MVP

### Catalogue public
- Liste des produits actifs.
- Liste des services actifs.
- Consultation des détails.
- Affichage des prix fixes ou de la mention « Prix sur demande » pour les services.

### Demandes clients
- Demande liée à un produit ou à un service.
- Nom, téléphone et message obligatoires.
- E-mail facultatif.
- Confirmation de l'enregistrement.

### Administration
- Création sécurisée du premier compte.
- Authentification.
- Gestion du catalogue.
- Gestion des demandes.
- Statuts : Nouvelle, En cours et Traitée.

Une demande traitée ne peut plus être rouverte.

## Règles importantes

- Seuls les produits et services actifs sont visibles publiquement.
- Une demande ne peut pas être enregistrée pour un produit ou service inactif.
- Les clients n'ont pas besoin de compte.
- Les produits et services sont désactivés plutôt que supprimés définitivement.
- Les demandes historiques sont conservées.
- Un seul compte administrateur est autorisé dans le MVP.
- Le premier compte administrateur nécessite un code d'activation.
- L'inscription initiale est fermée après la création de ce compte.
- Les services peuvent avoir un prix fixe ou un prix communiqué sur demande.

Le détail complet des 19 User Stories et des 15 règles métier se trouve dans `docs/user-stories/backlog-fonctionnel.md`.

## Technologies

| Composant | Technologie |
|---|---|
| Frontend | React + JavaScript |
| Backend | Python + FastAPI |
| Base de données | PostgreSQL |
| API | REST |
| Documentation API | Swagger / OpenAPI |
| Tests backend | Pytest |
| Conteneurisation | Docker |
| Versionnement | Git / GitHub |

## Architecture générale

- **Frontend React :** interface publique et espace d'administration.
- **Backend FastAPI :** API, authentification, validations et règles métier.
- **PostgreSQL :** stockage des produits, services, comptes et demandes.

Le backend est responsable de l'application des règles métier et de la protection des données.

## Structure du projet

```text
techcare-maintenance-system/
├── backend/
├── frontend/
├── docs/
│   └── user-stories/
│       └── backlog-fonctionnel.md
├── infrastructure/
├── README.md
└── .gitignore
```

Cette structure évoluera progressivement au fil de l'implémentation.

## Périmètre futur

Les fonctionnalités suivantes ne font pas partie du MVP initial, mais pourront être ajoutées ultérieurement :

- Paiement en ligne.
- Livraison.
- Multi-vendeurs.
- Application mobile.
- Gestion avancée des stocks.
- Facturation avancée.
- Notifications SMS et WhatsApp.
- Plusieurs comptes administrateurs.

## Objectif de réalisation

Développer TechCare Mini de manière progressive, en respectant les étapes suivantes :

1. Analyse fonctionnelle.
2. Conception des maquettes.
3. Conception de l'architecture et de la base de données.
4. Développement backend.
5. Développement frontend.
6. Tests et sécurisation.
7. Conteneurisation avec Docker.
8. Déploiement en production.
9. Vérifications, documentation et maintenance.

**Statut actuel :** revue fonctionnelle des 19 User Stories terminée. Prochaine étape : conception des maquettes et de l'architecture technique.