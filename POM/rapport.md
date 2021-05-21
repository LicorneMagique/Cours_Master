# Rapport

## Contexte des projets

Finalgo est une startup spécialisée dans

- la recherche de financements,
- la construction et la gestion de dossiers de financement,
- la recherche de subvention.

Nous développons des applications web pour répondre à ces besoins en SaaS<sup>1</sup>, nos clients ont donc un abonnement payant pour accéder à ces plateformes.

Cette année j'ai participé au développement des quatre projets principaux de Finalgo,

- **Main** notre application de construction et de gestion de dossiers de financement,
- **Crossroads Financing** notre application de recherche de financements,
- **Crossroads Subvention** notre application de recherche de subventions,
- **Finsearch** une sorte de Main simplifié dont nous gérons le développement et la maintenance pour l'un de nos clients.

1 : *Software as a service*

En terme de code chaque application possède un front Angular et un back Java Spring qui fonctionne sous forme d'une API REST. Le back est le même pour Main et pour Crossroads, puis Finsearch possède un front et un back ce qui nous fait 5 projets.

![.](projets.svg)

\* Les doubles flèches symbolisent les échanges de données entre front et back

---

## Tâches

### Tâche Finsearch

finsearch : parler de l'écran backoffice + du dev persistance plateforme de connexion des utilisateurs

### Tâche SSO

- SSO Cafpi
- SSO Crossroads Intuit
- SSO Crossroads Google
- Refacto : enum générique, getJsonObjectFromPath

On m'a confié toutes les tâches relatives au SSO (Single Sign-On), l'objectif de ces tâches est de permettre aux utilisateurs de se connecter sur nos plateformes à partir de leurs comptes déjà existants sur d'autres plateformes comme Google ou Microsoft.

*Image bouton se connecter avec Google*

#### Cafpi

J'ai commencé par implémenter le SSO pour l'un des clients de Main, leur entreprise utilise la suite Microsoft Azure qui permet la mise en place du SSO pour ses employés.

Dans un premier temps j'ai ajouté la page de connexion spécifique sur le front, Microsoft fournit une librairie qui permet de rediriger les utilisateurs sur leur page de connexion. Pour l'utiliser il suffit de l'ajouter à la page puis de l'appeler avec des identifiants prédéfinis que notre client nous a fournit. Ensuite la librairie nous retourne le JWT de l'utilisateur, que nous devons utiliser afin de valider sa connexion.

Une fois le JWT récupéré, le front le transmet au back qui le vérifie puis connecte l'utilisateur. Pour vérifier ce JWT il faut utiliser sa clé publique de Microsoft accessible sur l'API de Microsoft. J'ai codé une fonction qui se charge de récupérer cette clé. D'abord elle récupère la liste des clés publiques de Microsoft, puis elle utilise le `Key ID` (kid) présent dans l'entête du token afin de trouver la clé correspondante. Une fois récupérée j'ai utilisé la librairie `X.509` de Java Spring pour vérifier la signature du token, puis sa date de validité. Une fois que le token est validé, le back retourne un nouveau JWT au front qui est maintenant connecté.

#### Crossroads

ajout de la connexion sso de Google (back et front)
Mise en place d'une connexion SSO OAUTH2 avec la plateforme Quickbooks / Intuit

#### Refacto global à Cafpi et à Crossroads

réécriture du code de sso à l'aide d'un component spécifique (front)
factorisation des fonctions de vérification des tokens sso de Google Microsoft (back)
factorisation des fonctions de traitement des connexion sso d'intuit et de Google (back)

### Tâche antivirus

- Code front
- Code back
- Page wiki
- Cron
- Logs

MAJ du code antivirus (main back)

Mise en place du redémarrage et des mises à jour automatique du service antivirus sur notre serveur

### IText

- fichiers json

Implémentation d'un système générique pour la génération de la couverture des notes de synthèse avec du contenu dynamique, librairie IText

### Produit subvention

#### Mise en place back

Mise en place d'un service Java permettant de manipuler l'API REST Open Data du site aides-entreprises.fr
Mise en place d'une API de recherche des subventions
Mise en place d'un algorithme de filtre des subventions en fonction des réponses de l'utilisateur

#### Mise en place front

##### Refactoring

Réécriture du formulaire de recherche de financements dans le but de séparer la partie formulaire générique de la partie recherche de financements
Réécriture de la page résultats dans le but de séparer la partie page de résultats générique de la partie résultats de financements

##### Formulaire générique

Ajout d'options pour passer certaines questions en choix multiple
Ajout d'une barre de recherche sur les questions de type dropdown
Implémentation d'un système de sauvegarde des captions des réponses du formulaire

##### Formulaire spécifique

Création d'un nouveau formulaire de recherche de suventions pour les entreprises
Mise en place d'un système de questions dynamiques dont une partie du contenu est récupéré depuis l'API de recherche des subventions
Création d'une nouvelle page de résultats pour les subventions
Implémentation d'un mode debug qui affiches des informations spécifiques aux subventions
Création d'un algorithme de recherche de contact dans les données de l'API (que Bertrand a corrigé)

#### Génération des statistiques

Génération de statistiques de pertinence des critères de filtre des subvention
Révision de la priorité de chaque critère de filtre des subvention en fonction de ces résultats
Page wiki
J'ai mangé leur BD avec Postman
Traitement / analyse des données de l'API subvention, notamment des territoires avec PostMan
Mettre ma requête trop cool de BD

#### Améliorations

##### Moins de travail pour l'utilisateur mais autant de données

Préciser quand même que c'est en pause et planté depuis un moment

Dans le formulaire des subvention, remplissage automatique de certaines questions à partir des informations du code siret qu'on récupère depuis l'API de l'INSEE
Création de table de convertion code effectif siret -> code effectif aides-entreprises et code postal -> code territoire aides-entreprises
ajout des informations récupérées par le code siret dans le mode debug du front (front et back)
récupération automatique du profil aides-entreprises à partir du numéro de siret (back)

##### Recherche naïve par mots clés

ajout d'un système de recherche de subvention par mots clés (back)
ajout de la question pour récupérer les mots clés (front)
ajout d'un système de niveau de priorité des paramètres aides-entreprises pour améliorer l'algorithme de relachement des contraintes

##### Indépendance de l'API

Ajout système de copie quotidien de la base de données des subventions avec un cron
Enregistrement de certaines informations des subventions dans notre base de données
Envoi de ces informations à notre front
Ajout d'un système de traitement spécifique des subventions pour ajouter de nouveaux critères que l'API aides-entreprises.fr ne prend pas en charge

###### Pour aller encore plus loin

Création d'un algorithme de nettoyage des caractères spéciaux dans le texte : balises html, escape html, escape unicode
Récupération de tous les mots distincts utilisés dans la base de données subvention, avec un objectif d'IA sur les mots

### Stripe

Refactoring du système de gestion des acticles Stripe pour quelque chose de plus généique et typé (permettant de détecter plus d'erreurs qu'avant) (crossroads)
Réimplémentation de toute l'API Stripe avec la dernière version, l'ancienne version était complètement dépréciée (crossroads)

Récupération automatique des captions des utilisateurs depuis leur facture Stripe
Debug de Stripe dont le callback était bloqué par notre JwtFilter

### Fonctionnalités spécifiques diverses

#### Système d'unité des OCA

Ajout d'un système d'unité (mois, %, €, année(s)) dans les OCA (système de stockage ressemblant à du NoSQL) (main back)

Ajout du système d'unité des OCA sur les ITE (propagation du système d'unité dans le front) (main front)

#### Conservation du GET sur Crossroads

Ajout d'un système de conservation des paramètres GET de l'URL

#### Génération enum depuis csv d'Araud

génération d'une class enum java à partir d'un fichier csv et de nodejs

#### Fix session context -> request context

Fix du problème de récupération de l'utilisateur connecté en back (bug avec les variables de session partagées)

---

## Retour d'expérience

Ça m'a appri

- à coder en PL-SQL sur un serveur MySQL 8
- à coder au debugger
- à coder du code qui résiste au segfault
- à coder plus simple et plus générique et à compiler le spécifique dans un coin genre un enum
- la création, la mise en place, la vente et l'évolution d'un produit de A à Z en mode MVP
- à lire une doc, genre beaucoup trop de docs, mais aussi à pas trop les lire et surtout à regarder stack overflow
- à sérieusement mieux utiliser git, au sens commiter les bonnes lignes uniquement, abuser du stash et des branches, abuser du merge --no-commit, globalement abuser de l'interface graphique
- à never trust the user même si le user c'est moi
- à documenter mon travail (commentaires mais surtout wiki)
- à définir un lexique et essayer de le respecter histoire que toute l'équipe comprenne de quoi on parle
