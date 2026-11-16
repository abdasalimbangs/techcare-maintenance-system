# Modèle de données — TechCare Mini

## 1. Présentation

Ce document décrit la conception de la base de données de TechCare Mini, une mini-marketplace permettant aux visiteurs de consulter les produits et services d'une entreprise et d'envoyer des demandes.

La base de données utilise PostgreSQL.

Le MVP repose sur quatre tables principales :

- ADMINISTRATEUR
- PRODUIT
- SERVICE
- DEMANDE

Le modèle est conçu pour garantir la cohérence des données, préserver les demandes historiques et faciliter les évolutions futures de l'application.

## 2. Table ADMINISTRATEUR

Cette table contient les informations du compte administrateur de l'entreprise.

| Attribut | Type logique | Obligatoire | Contraintes |
|---|---|---|---|
| administrateur_id | BIGINT | Oui | Clé primaire, générée automatiquement |
| nom | Texte | Oui | |
| prenom | Texte | Oui | |
| email | Texte | Oui | Unique |
| telephone | Texte | Oui | |
| mot_de_passe_hash | Texte | Oui | Contient uniquement le mot de passe haché |
| adresse | Texte | Non | |
| photo_profil | Texte | Non | Chemin ou adresse du fichier |
| date_creation | Date et heure | Oui | Générée automatiquement |
| date_modification | Date et heure | Oui | Mise à jour automatiquement |

### Règles particulières

- L'adresse e-mail doit être unique.
- Le mot de passe ne doit jamais être enregistré en clair.
- Le champ `mot_de_passe_hash` contient uniquement une version sécurisée du mot de passe.
- Le code d'activation utilisé pour créer le premier administrateur est conservé dans la configuration secrète du serveur et non dans cette table.
- L'inscription initiale est autorisée uniquement si aucun administrateur n'existe déjà.
- Le MVP prévoit un seul compte administrateur.

## 3. Table PRODUIT

Cette table contient les produits proposés par l'entreprise.

| Attribut | Type logique | Obligatoire | Contraintes |
|---|---|---|---|
| produit_id | BIGINT | Oui | Clé primaire, générée automatiquement |
| administrateur_id | BIGINT | Oui | Clé étrangère vers ADMINISTRATEUR |
| nom | Texte | Oui | |
| description | Texte long | Oui | |
| prix_actuel | Décimal | Oui | Prix en GNF, strictement supérieur à zéro |
| photo | Texte | Oui | Chemin ou adresse d'une seule photo pour le MVP |
| etat_disponibilite | Texte contrôlé | Oui | DISPONIBLE, RUPTURE_STOCK ou SUR_COMMANDE |
| est_actif | Booléen | Oui | Vrai par défaut |
| date_creation | Date et heure | Oui | Générée automatiquement |
| date_modification | Date et heure | Oui | Mise à jour automatiquement |

### Règles particulières

- Chaque produit doit être associé à un administrateur existant.
- Le prix actuel doit être strictement supérieur à zéro.
- Un produit actif mais en rupture de stock reste visible publiquement avec la mention « Rupture de stock ».
- Un produit actif avec l'état `SUR_COMMANDE` reste visible publiquement avec la mention « Sur commande ».
- Un produit désactivé est masqué du catalogue public.
- Un produit désactivé reste conservé dans la base de données et peut être réactivé.
- Les anciennes demandes associées au produit doivent être conservées.
- La désactivation ne doit jamais entraîner la suppression physique du produit.

Le champ `est_actif` est indépendant du champ `etat_disponibilite`.

## 4. Table SERVICE

Cette table contient les prestations proposées par l'entreprise.

| Attribut | Type logique | Obligatoire | Contraintes |
|---|---|---|---|
| service_id | BIGINT | Oui | Clé primaire, générée automatiquement |
| administrateur_id | BIGINT | Oui | Clé étrangère vers ADMINISTRATEUR |
| nom | Texte | Oui | |
| description | Texte long | Oui | |
| type_tarification | Texte contrôlé | Oui | PRIX_FIXE ou PRIX_SUR_DEMANDE |
| prix | Décimal | Selon le type | Obligatoire si PRIX_FIXE |
| photo | Texte | Oui | Chemin ou adresse d'une seule photo pour le MVP |
| etat_disponibilite | Texte contrôlé | Oui | DISPONIBLE ou INDISPONIBLE |
| est_actif | Booléen | Oui | Vrai par défaut |
| date_creation | Date et heure | Oui | Générée automatiquement |
| date_modification | Date et heure | Oui | Mise à jour automatiquement |

### Règles particulières

- Chaque service doit être associé à un administrateur existant.
- Lorsque `type_tarification = PRIX_FIXE`, le prix est obligatoire et doit être strictement supérieur à zéro.
- Lorsque `type_tarification = PRIX_SUR_DEMANDE`, le champ `prix` doit obligatoirement être `NULL`.
- Lorsqu'un service passe de `PRIX_FIXE` à `PRIX_SUR_DEMANDE`, l'ancien prix doit être effacé et remplacé par `NULL`.
- Lorsqu'un service passe de `PRIX_SUR_DEMANDE` à `PRIX_FIXE`, l'administrateur doit saisir un nouveau prix valide.
- Un service actif mais indisponible reste visible publiquement avec la mention « Indisponible ».
- Un service désactivé est masqué du catalogue public.
- Un service désactivé reste conservé dans la base de données et peut être réactivé.
- Les anciennes demandes associées au service doivent être conservées.
- La désactivation ne doit jamais entraîner la suppression physique du service.

Le champ `est_actif` est indépendant du champ `etat_disponibilite`.

## 5. Table DEMANDE

Cette table enregistre les demandes envoyées par les visiteurs.

Le visiteur n'a pas besoin de créer un compte pour envoyer une demande.

| Attribut | Type logique | Obligatoire | Contraintes |
|---|---|---|---|
| demande_id | BIGINT | Oui | Clé primaire, générée automatiquement |
| nom_client | Texte | Oui | |
| telephone_client | Texte | Oui | |
| email_client | Texte | Non | |
| message | Texte long | Oui | |
| statut | Texte contrôlé | Oui | NOUVELLE par défaut |
| produit_id | BIGINT | Selon le cas | Clé étrangère facultative vers PRODUIT |
| service_id | BIGINT | Selon le cas | Clé étrangère facultative vers SERVICE |
| date_creation | Date et heure | Oui | Générée automatiquement |
| date_modification | Date et heure | Oui | Mise à jour automatiquement |

### Règles particulières

- Une demande doit obligatoirement concerner un produit ou un service.
- Une demande ne peut jamais concerner simultanément un produit et un service.
- Une demande ne peut pas être enregistrée sans produit ni service associé.
- Le visiteur doit renseigner son nom, son numéro de téléphone et son message.
- L'adresse e-mail est facultative.
- Une demande concernant un produit ou un service inactif doit être refusée.
- Une demande concernant un produit en rupture de stock ou un service indisponible reste autorisée si le produit ou le service est encore actif.
- Les demandes historiques doivent être conservées même lorsque le produit ou le service concerné est désactivé.

### Statuts possibles

Les statuts autorisés sont :

- `NOUVELLE`
- `EN_COURS`
- `TRAITEE`

Le statut initial d'une demande est `NOUVELLE`.

Les transitions autorisées sont :

`NOUVELLE` → `EN_COURS` → `TRAITEE`

Une demande ne peut pas passer directement de `NOUVELLE` à `TRAITEE`.

Une demande ayant le statut `TRAITEE` ne peut plus changer de statut. Elle reste consultable dans l'espace administrateur.

## 6. Relations entre les tables

| Relation | Cardinalité | Explication |
|---|---|---|
| ADMINISTRATEUR — PRODUIT | 1 à N | Un administrateur peut créer plusieurs produits. Chaque produit est associé à un seul administrateur. |
| ADMINISTRATEUR — SERVICE | 1 à N | Un administrateur peut créer plusieurs services. Chaque service est associé à un seul administrateur. |
| PRODUIT — DEMANDE | 1 à N | Un produit peut recevoir plusieurs demandes. Chaque demande peut être associée à un seul produit. |
| SERVICE — DEMANDE | 1 à N | Un service peut recevoir plusieurs demandes. Chaque demande peut être associée à un seul service. |

Dans ces relations, un administrateur, un produit ou un service peut exister sans avoir encore de produit, de service ou de demande associé.

Une demande est obligatoirement associée à exactement un produit ou un service.

Il n'existe pas de relation directe entre ADMINISTRATEUR et DEMANDE dans le MVP.

## 7. Règles d'intégrité et de gestion

Les règles suivantes doivent être respectées par l'application et, lorsque cela est possible, protégées directement par PostgreSQL.

1. Un produit doit être associé à un administrateur existant.
2. Un service doit être associé à un administrateur existant.
3. Une demande doit être liée à exactement un produit ou un service.
4. Une demande concernant un produit ou service inactif doit être refusée.
5. Seuls les produits et services actifs sont visibles dans le catalogue public.
6. L'état de disponibilité est indépendant de l'activation.
7. La désactivation ne supprime jamais définitivement un produit ou un service.
8. Les demandes historiques sont conservées.
9. Le prix d'un produit doit être strictement supérieur à zéro.
10. Le prix d'un service est obligatoire et strictement positif lorsque le type de tarification est `PRIX_FIXE`.
11. Le prix d'un service doit être `NULL` lorsque le type de tarification est `PRIX_SUR_DEMANDE`.
12. Une demande ayant le statut `TRAITEE` ne peut plus changer de statut.
13. Les mots de passe ne sont jamais stockés en clair.
14. Les clés étrangères doivent préserver l'intégrité des relations.
15. Les identifiants des quatre tables principales utilisent le type `BIGINT`.
16. Les clés étrangères correspondantes utilisent également le type `BIGINT`.

### Contraintes à imposer dans PostgreSQL

Les contraintes suivantes devront être mises en place directement dans la base de données :

**Contrainte sur les prix des produits :**

`prix_actuel > 0`

**Contrainte sur les prix des services :**

- Si `type_tarification = PRIX_FIXE`, alors `prix > 0`.
- Si `type_tarification = PRIX_SUR_DEMANDE`, alors `prix IS NULL`.

**Contrainte sur les demandes :**

Une seule des deux clés étrangères `produit_id` et `service_id` doit être renseignée.

Cette règle devra être protégée par une contrainte `CHECK` dans PostgreSQL et vérifiée également par le backend FastAPI.

### Protection des données historiques

Les produits et services associés à des demandes historiques ne doivent pas être supprimés physiquement.

La désactivation logique avec le champ `est_actif` est utilisée à la place d'une suppression définitive.

Les clés étrangères devront empêcher la suppression physique d'un produit ou service encore référencé par une demande.

## 8. Éléments reportés après le MVP

Pour respecter le délai de développement d'un mois, les fonctionnalités suivantes sont reportées :

- Plusieurs photos par produit ou service.
- Notes internes sur les demandes.
- Plusieurs administrateurs.
- Historique détaillé des modifications de prix.
- Gestion avancée des remises.
- Gestion avanc