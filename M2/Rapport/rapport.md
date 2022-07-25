# Rapport final d'alternance

Ce document est un brouillon du rapport final.

## Page de garde

Titre :

> Rapport d'alternance  
> développeur full stack  
> chez Finalgo

Bloc "réalisé par / tuteurs"

> Réalisé par : Julien Giraud  
> Diplôme préparé : Master 2 Informatique  
> Tuteur entreprise : Bertrand Héllion  
> Tuteur pédagogique : Lionel Médini  
> Durée : du 06/09/2021 au 31/08/2022 (2 an)

## Remerciements

Pour commencer je tiens à remercier toute l'équipe de Finalgo ainsi que les dernières générations de stagiaires et alternants pour m'avoir intégré, accompagné et partagé leur bonne humeur au cours de ces deux dernières années.

En particulier je remercie Bertrand Hellion de m'avoir accepté à Finalgo et encadré tout au long de mon alternance. À ses côtés j'ai acquis de nombreuses compétences comme écrire du code robuste, utiliser le plus possible la généricité et avoir un esprit critique sur les missions à réaliser.

Enfin, je remercie Lionel Médini d'avoir été mon tuteur cette année et de m'avoir aidé à la rédaction de ce rapport.

## Table des matières

- [Rapport final d'alternance](#rapport-final-dalternance)
  - [Page de garde](#page-de-garde)
  - [Remerciements](#remerciements)
  - [Table des matières](#table-des-matières)
  - [Glossaire](#glossaire)
  - [Introduction](#introduction)
  - [Présentation de Finalgo](#présentation-de-finalgo)
    - [L'équipe](#léquipe)
    - [Les projets](#les-projets)
  - [Environnement de travail](#environnement-de-travail)
    - [Matériel et lieu](#matériel-et-lieu)
    - [Outils et logiciels](#outils-et-logiciels)
      - [Slack](#slack)
      - [Asana](#asana)
      - [Google Workspace](#google-workspace)
      - [Gather](#gather)
  - [Environnement technique](#environnement-technique)
    - [Côté serveur](#côté-serveur)
    - [Côté client](#côté-client)
    - [Outils de développement](#outils-de-développement)
  - [Travail réalisé](#travail-réalisé)
    - [Notre modèle de données](#notre-modèle-de-données)
    - [Problèmes de l'ancienne implémentation](#problèmes-de-lancienne-implémentation)
    - [Travail réalisé](#travail-réalisé-1)
    - [Procédure de refactoring et migration](#procédure-de-refactoring-et-migration)
    - [Retours sur cette mission](#retours-sur-cette-mission)
  - [Conclusion](#conclusion)
  - [Annexes](#annexes)

## Glossaire

| Terme | Définition |
| ----- | ---------- |
| Angular | Angular est un framework MVC basé sur TypeScript, développé par Google et utilisé pour la création d’applications web. Ce type d'application possède la particularité de mettre à jour le visuel d’un site internet sans recharger la page. C'est ce qu'on appel une Single Page Application (SPA). |
| API | Une API (Application Programming Interface) est un programme qui permet à des applications différentes de communiquer ensemble afin d’échanger des données. |
| Back-End | Désigne l'ensemble des traitements effectués côté serveur afin de permettre le bon fonctionnement d'une application. |
| Composant | Dans Angular, un composant est un ensemble formé d’une page HTML, d’un fichier CSS et d’une classe TypeScript. Plus précisément, il s’agit d’une entité réutilisable et les pages sont des composants, eux-mêmes formés de plusieurs composants. |
| Enum | Un enum est un type de donnée contenant un nombre fixe de valeurs constantes. |
| Financement alternatif | Système de financement qui ne repose pas sur les systèmes financiers traditionnels comme les banques réglementées et les marchés de capitaux. Par exemple les prêts à la consommation en ligne, les fonds de prêt aux entreprises en ligne et affacturage ou le financement participatif (crowdfunding). |
| FinTech | Une FinTech est un mot formé par les termes « finance » et « technologie ». Il désigne des entreprises innovantes qui proposent des services financiers à l’aide des nouvelles technologies. |
| Framework | Un Framework est un ensemble d’outils à la base d’une application qui simplifie le travail des développeurs informatiques. |
| Front-End | Désigne le visuel et l'ensemble des traitements réalisés par une application web côté client, c'est à dire depuis un navigateur web. |
| Map | Une map est un type de données qui relie un ensemble de clés à un ensemble de valeurs. |
| Mise en production | Une mise en production est un procédé permettant de déployer une nouvelle version d’une application. |
| SaaS | Le SaaS « software as a service » est un logiciel hébergé par un tiers et accessible à distance. Généralement, cette solution est facturée sous la forme d’un abonnement mensuel. |
| Service | Un service est une instance d’une classe TypeScript injectable dans tous les composants d’une application pour les aider à communiquer entre eux. Cette classe centralise les données et facilite la réutilisation de code. |
| TypeScript | TypeScript est un langage de programmation développé par Microsoft. C’est un sur-ensemble de JavaScript qui introduit de nouvelles fonctionnalités comme le typage ou la programmation orientée objet. Le code est transcompilé en JavaScript et donc interprétable avec n’importe quel navigateur web ou moteur JavaScript. |

## Introduction

Dans le cadre de mon Master Informatique à l'UCBL j'ai opté pour un cursus en alternance au sein de Finalgo, une startup locale spécialisée dans les applications web en lien avec les financements.

J'ai pu effectuer cette alternance suite à mon stage optionnel de L3 réalisé au même endroit. Pour celle-ci, un contrat d'apprentissage de deux ans a été signé. Cette période correspond à un Master qui se termine par un diplôme dans les Technologies de l'Information et Web (TIW).

Les notions vues en cours lors de mon DUT, de ma Licence 3 et tout au long du Master ainsi que mes précédentes expériences professionnelles m'ont beaucoup aidé à réaliser mes missions en entreprise.

Certaines missions ont renforcé mes connaissances, d'autres m'ont permi de comprendre des éléments abordés au cours de l'année dans un cadre professionnel.

Tout au long de l'année j'ai réalisé des missions diverses au sein de Finalgo, principalement dans le but de **réduire la dette technique et améliorer les performances de nos applications**.

## Présentation de Finalgo

Finalgo est une FinTech familiale de 8 collaborateurs spécialisée dans la recherche de financements 100 % digitale ainsi que la construction et la gestion de dossiers de financement.

Notre vocation est de faciliter l'accès au financement pour les entrepreneurs, artisans, commerçants et plus généralement aux dirigeants de TPE / PME.

Nous proposons à nos clients trois plateformes web en SaaS qui répondent à ces besoins. La première est un outil de gestion pour les professionnels de la finance, elle permet de construire et gérer des dossiers de financement et fonctionne sous forme d'abonnements payants. La deuxième est à destination des dirigeants de TPE / PME, elle permet de rechercher gratuitement des financements alternatifs sur lesquels nous prenons une comission lorsqu'un partenaire finance le projet. La dernière permet de remplir et de suivre les demandes de financements, elle sert d'intermédiaire entre les dirigeants et nos partenaires financiers qui accordent les financements.

![Expertise financement](assets/expertise-financement.png)

### L'équipe

À Finalgo la hiérarchie est très horizontale. Les cofondateurs font partie intégrante des équipes en plus d'avoir un rôle de manager, et tout le mode a la possibilité d'exprimer ses idées.

![organigramme](./assets/organigramme.svg)

\* Non présents en même temps

### Les projets

Cette année mes missions ont porté sur les trois principaux projets de Finalgo,

- **Main** notre application de construction et de gestion de dossiers de financement pour les professionnels de la finance,
- **Automate** notre application de recherche de financements alternatifs,
- **Advisor** notre application de gestion, de suivi et d'envoi de demandes de financement alternatifs pour les dirigeants de TPE / PME.

En terme de projets informatiques, toutes les plateformes possèdent un Front-End Angular et elles communiquent avec le même Back-End. La description détaillée de l'architecture se trouve dans la partie [Environnement technique](#environnement-technique).

## Environnement de travail

### Matériel et lieu

À Finalgo nous travaillons beaucoup en télétravail. Lorsque nous allons dans les locaux, deux à trois fois par semaine pour les membres de l'équipe qui sont à proximité de Lyon, nous allons au HUB612. Il s'agit d'un incubateur, une sorte d'open space avec une équipe qui accompagne les entreprises. Le HUB612 est spécialisé dans les entreprises qui travaillent sur la finance, les assurances et le marketing à l'aide d'outils numériques modernes. C'est un lieu agréable pour travailler et échanger avec des personnes dans des domaines similaires aux nôtres.

![hub](assets/hub.png)

Pour travailler on a mis à ma disposition un ordinateur portable avec une très bonne configuration, ce qui me permet d'utiliser efficacement tous les logiciels dont j'ai besoin. J'utilise généralement un deuxième écran pour des questions de confort, il y en a sur les bureaux du HUB* et j'utilise mon écran personnel en télétravail.

### Outils et logiciels

Depuis le début de la crise sanitaire, toute notre organisation est basée sur du travail en distanciel. Nous sommes donc équipés en outils de communication, visioconférence, gestion des tâches et suite de bureautique.

#### Slack

<img alt="slack" src="./assets/slack.svg" width="64"> Slack est notre outil de messagerie interne.

<img alt="slack" src="./assets/channels.png" width="90" style="float: left; margin-right: 3em">

Nous avons un espace de travail "Finalgo" avec des **canaux de discussion** pour tous les sujets, ce qui permet de configurer les notifications qu'on souhaite recevoir pour chaque type d'information.

Il y a un canal pour

- chaque **projet** : Back-End, Automate, Advisor
- chaque **domaine** : informatique, marketing, communication, design, recrutement, teambuilding…
- chaque **type de logs** : bugs utilisateurs, boutons "demander de l'aide", actions utilisateurs, actions nécesitant une intervention de notre part, traces des différents serveurs de production et de développement…
- la **détente** : on y trouve des blagues ou liens en tout genre pour partager de la bonne humeur avec l'équipe.

#### Asana

<img alt="asana" src="./assets/asana.svg" width="64"> Asana est notre plateforme de gestion des tâches.

La plateforme permet de créer des projets qui fonctionnent comme les tableaux sur Trello. Il est possible d'y créer des colonnes et d'y ajouter des tâches avec des attributions, des images, des sous-tâches.

Nous utilisons ces tableaux pour remplacer le **Scrum Board**, un tableau de post-it utilisé par la méthode SCRUM qui est à l'origine de notre méthode de travail. Grâce à ces tableaux nous pouvons voir qui travail sur une tâche, connaître son avancement, en ajouter nous-même et écrire les spécification. Il y a beaucoup plus de fonctionnalités sur le site mais nous n'en avons pas encore l'utilité.

#### Google Workspace

<img alt="gmail" src="./assets/gmail.svg" width="64"> | <img alt="drive" src="./assets/drive.svg" width="64"> | <img alt="meet" src="./assets/meet.svg" width="64"> | <img alt="calendar" src="./assets/calendar.svg" width="64"> | <img alt="sites" src="./assets/sites.svg" width="48"> | <img alt="sheets" src="./assets/sheets.svg" width="48"> |
| ----- | ----- | ---- | -------- | ----- | ------ |
| Gmail | Drive | Meet | Calendar | Sites | Sheets |

Finalgo utilise un système de comptes Google pour les entreprises. Nos comptes nous permettent d'accéder à la suite de bureautique comme avec une adresse **Gmail** classique, même s'ils terminent par `@finalgo.fr`. Toutes ces applications sont liées à un espace partagé sur **Google Drive**, auquel nous avons tous accès avec notre compte.

**Meet** est une plateforme de réunions numériques très simple à utiliser. Il est possible de se connecter à un salon grâce à un lien, on peut ensuite participer avec sa caméra, son micro ou en faisant des partages d'écran. Nous utilisons Meet pour les réunions clients.

**Calendar** est un agenda, il sert surtout à planifier des rendez-vous clients ou des points d'équipe importants. Un salon meet est associé à chaque événement de l'agenda. Ce système évite de générer un lien et de l'envoyer aux invités, il suffit de les ajouter sur un événement.

**Google Sites** sert exclusivement à voir et alimenter notre wiki interne. Il s'agit d'un site accessible uniquement avec notre compte, sur lequel nous répertorions toutes sortes d'informations utiles pour Finalgo. On y trouve les procédures comme les mises en production, les installations, les plateformes et il y a des explications sur les technologie inhabituelles. C'est un outil que nous utilisons et alimentons beaucoup, il entre dans la philosophie SCRUM en facilitant les formations mutuelles au sein de l'équipe.

**Sheets** est un tableur comme Excel, nous l'utilisons en interne et en externe. Il y a des tableaux administratifs pour gérer des choses comme les congés, certains servent d'outils de maintenance et ticketing, d'autres permettent de synthétiser des informations afin de les exporter dans le code.

#### Gather

![gmail](./assets/gather.png)

Gather est notre outil de communication interne n°1. Comme Slack, nous sommes connecté toute la journée sur cette plateforme qui permet de se déplacer dans un monde virtuel 2D et d'effectuer des visioconférences.
Etant donné que tous les membres de l’équipe ne résident pas à Lyon, cet outil permet de rester en constante communication avec eux malgré la distance.  
Chaque personne a son propre bureau virtuel et des pièces spécifiques ont été créées pour remplir différentes fonctions : cafétéria pour discuter en arrivant au travail, salle de réunion, jardin pour jouer à des mini-jeux, ect.

## Environnement technique

### Côté serveur

Pour les serveurs nous avons un compte sur la plateforme OVH avec une dizaine de VPS (virtual private server) sous Debian.

Sur ces VPS nous avons un serveur Apache pour servir le Front-End compilé par Angular et un serveur Tomcat pour le Back-End Java Spring Boot.

Nos projets Spring Boot utilisent Java version 11 avec divers dépendances. Voici un résumé des plus utilisées et de celles que j'ai utilisées.

| Dépendance | Description |
| ---------- | ----------- |
| Auth0 | Librairie qui permet de manipuler les JWT. |
| Hibernate / HQL | Framework qui permet de manipuler la base de données à travers des interfaces. Il implémente le HQL, un langage de requête de base de données relationnelles similaire à SQL avec une approche orientée objet. |
| Swagger | Une interface qui permet de visualiser l'architectures d'une API et d'y envoyer des requêtes. |
| JSONObject | Une librairie qui permet de manipuler facilement des objets JSON |

Il y a d'autres programmes installés sur les serveurs, les plus importants sont les suivants.

MySQL : système de gestion de bases de données relationnelles.

Cron : programme qui permet de programmer l'exécution de scripts ou de logiciels sur Linux.

![serveurs](assets/serveurs.svg)

Il existe une réplication de cette architecture avec uniquement la plateforme Main en Front-End pour l'un de nos clients, nous utilisons un profil Spring pour effectuer la distinction dans le Back-End.

![picto gris](./assets/picto-gris.png) Échanges internes au serveur.  
![picto bleu](assets/picto-bleu.png) Échanges HTTP entre la SPA de la plateforme et le Back-End.  
![picto rouge](./assets/picto-rouge.png) Point d'entrée du serveur via les requêtes HTTP.

### Côté client

En Front-End nous utilisons Angular 11, un framework open source de Google basé sur le langage TypeScript. Le code HTML Angular utilise une syntaxe enrichie par rapport au HTML5, il est possible d'y insérer des éléments de code. Il y a également une prise en charge du langage Saas qui permet de simplifier la syntaxe du CSS. Nous utilisons la version SCSS de Saas car sa syntaxe inclue celle du CSS, ainsi il est possible d'écrire du SCSS ou du CSS dans les fichiers de style.

TypeScript est un langage de programmation libre et open source de Microsoft. Ce langage est basé sur JavaScript avec un système de typage, de classes et d'éritage similaire à celui de Java. Il est possible de convertir du code TypeScript en code JavaScript.

Notre projet Angular utilise divers dépendances. Voici un résumé des plus utilisées.

| Dépendance | Description |
| ---------- | ----------- |
| Bootstrap | Ensemble de classes CSS qui permettent de simplifier la mise en place du responsive design. |
| Forms | Ensemble de Classes et composants Angular qui permettent de gérer les formulaires. |
| Material | Ensemble de classes et composants Angular qui permettent de créer des interfaces graphiques d'application très facilement. |
| Router | Ensemble de classes et composants Angular qui permettent de gérer les routes d'une application et de manipuler l'URL. |
| SweetAlert2 | Librairie qui permet d'afficher toutes sortes de pop-up personalisables. |

### Outils de développement

De façon générale il y a beaucoup d'informations utiles pour le développement sur notre wiki. On y trouve notamment :

- les liens des swaggers
- la procédure d'installation d'un serveur
- la procédure de renouvellement des certificats
- les commandes à utiliser pour installer MySQL sur notre machine et y charger des données de test,
- la procédure à suivre pour mettre en production le Back-End ou le Front-End,
- la procédure à suivre pour accéder aux logs des applications de production,
- des explications sur nos modèles de données.

Pour développer en Front-End j'utilise Visual Studio Code comme IDE. Il s'agit d'un éditeur de code sur lequel on peut ajouter divers extensions pour simplifier le développement, notamment sur Angular. J'utilise également beaucoup les outils de développement de Google Chrome, dont le débugger permet de suivre l'éxécution du code TypeScript.

Pour le Back-End j'utilise l'IDE IntelliJ qui est très efficace pour le Java. J'utilise beaucoup le débugger de cet IDE, à la fois pour visualiser l'exécution du code ligne par ligne mais aussi pour tester en direct du code Java.

Nous utilisons un système de logs interne appelé "user actions". Ce système associe les données des logs à des "actions" réparties en catégories d'importance. De nombreux comportements de nos applications sont branchés sur ces actions qui sont enregistrées en base de données et envoyées sur les canaux Slack correspondants via leur API. De cette façon nous avons un accès rapide à l'activité des utilisateurs et aux comportements anormaux, ce qui facilite de débug.  
Il y a un canal par type d'importance et par serveur.

![logs](assets/logs.png)

*Apperçu des canaux de "user acion" sur Slack.*

Pour tous nos projets nous utilisons GIT comme gestionnaire de version et le code est sauvegardé en ligne sur GitHub. Nous avons tous un compte sur cette plateforme et nous avons les droits d'accès sur les différents projets, par défaut ils sont inaccessibles.  
Pour gérer les commits et les branches j'utilise une extension de Visual Studio Code qui propose une interface graphique. Elle permet d'effectuer toute sorte d'opération très facilement, en particulier de ne commiter que certaines lignes de code dans un fichier ou de visualiser les différences entre les commits.

![git_log](./assets/git_log.png)

Enfin, pour travailler sur les bases de données nous utilisons DBeaver, un logiciel libre avec une interface plutôt intuitive.

![dbeaver](./assets/dbeaver.png)

## Travail réalisé

Cette année j'ai surtout travaillé sur l'amélioration de notre système de données, en plus de diverses missions d'ajout ou d'évolution des fonctionnalités sur nos applications.

### Notre modèle de données

La plupart de nos objets métier ont les mêmes caractéristiques. Que ce soit un projet, un utilisateur ou une entreprise ; ils ont un identifiant, un nom, un état de suppression, divers autres champs et **une map de données associée à des propriétés**. Nous appelons ces propriétés les "OCA variables", il en existe des centaines pour toute sorte d'information et en théorie elles ne sont pas associées à un seul type d'objet métier. Elles permettent de stocker des propriétés comme le chiffre d'affaires d'un partenaire avec une clé pour chaque année connue, ou le code NAF d'une entreprise avec une seule clé.

```text
objet_métier_x(__id__, caption, deleted, autres_propriétés...)
oca_variable_x(__id__, #objet_métier_x_id, code_propriété, clé_propriété, valeur)
```

*Modèle relationnel utilisé*

```ts
var ocaVariables: Map<propriété, Map<clé, valeur>>
```

*Description du typage des OcaVariables*

Dans le code il existe un Enum qui renseigne les propriétés ainsi que le type des valeurs associées. Une classe abstraite se charge de manipuler la structure ce qui rend son utilisation très facile.

```java
person.getOcaVariables().addValue(Oca.object_creation_date, new Date());
```

Ce modèle est efficace pour stocker nos centaines de propriétés sans rendre les tables ou les requêtes illisibles du côté de la base de données. Son implémentation possède cependant une forte dette technique que j'ai remboursé pendant plusieurs mois.

### Problèmes de l'ancienne implémentation

En base de données, pour chaque objet métier il y avait une table pour l'objet et une table pour ses OCA variables soit une douzaine de tables. Plusieurs tables d'OCA n'avaient pas de clé étrangère et il n'y avait aucun index, ce qui causait une latence sur de nombreuses requêtes. Aussi, certains objets avaient des clés étrangères dans leur table qui étaient en doublon avec nos tables de jointure.

Dans les méthodes de service, tous les mécanismes des OCA variables n'étaient pas réalisés par la classe abstraite, ce qui était compensé par de la duplication de code avec des erreurs de mise à jour lors des évolutions.  
Ensuite la création, la modification et la suppression des OCA variables étaintt gérées par un service qui effectuait un appel à MySQL pour chaque clé de chaque propriété au lieu de tout envoyer d'un coup. Plusieurs services effectuaient également ce type d'appels en boucle pour divers traitements sur des collections d'objets métier. Ce type de comportement menait à des centaines voire des milliers d'échanges entre Spring et MySQL sur beaucoup de nos API, ce qui pernait parfois plusieurs dizaines de secondes voire quelques minutes.

Enfin, les clés étrangères en doublon étaient aléatoirement utilisées dans le code, ce qui portait à confusion.

### Travail réalisé

- Mettre en place une base propre
  - En base de données
    - Créer les table GENERIC_OBJECT et OCA_GENERIC_OBJECT
      - GENERIC_OBJECT(**id**, nom, type, état_suppression, ancien_id)
      - OCA_GENERIC_OBJECT(**id**, #generic_object_id, code_propriété, clé_propriété, valeur)
    - Ajouter les indexes pour toutes les combinaisons de colones
  - Dans le code Java
    - Créer les classes GenericObject, OcaGenericObject, GenericObjectService et GenericObjectDAO
    - Effectuer le mapping sur Hibernate pour GenericObject et OcaGenericObject
    - Identifier toutes les méthodes communes aux différents objets métiers ou à leurs services et les ajouter judicieusement dans les nouvelles classes 
- Préparer la migration de chaque objet métier
  - En base de données
    - Migrer les éventuelles clés étrangères vers les tables de jointure, ou les supprimer en cas de doublon
    - Migrer les autres colones vers la table d'OCA variables de l'objet
    - Supprimer les colones obsolètes
  - Dans le code Java
    - Utiliser les bonnes tables de jointure
    - Supprimer les "autres attributs" de classe et remplacer leur utilisation par celle des OCA variables, parfois tout est faisable à partir des getter/setter, parfois il faut modifier des méthodes de service
- Migrer les objets sur la nouvelle base
  - En base de données
    - Effectuer la migration...
    - 
- Mettre à jour le mapping des objets métiers pour qu'ils étendent la classe GenericObject et utilisent la nouvelle table d'OCA variables

### Procédure de refactoring et migration

-> Dire que pendant le refactoring j'ai recherché les fonctions qui faisaient des appels en boucle à la base de données

### Retours sur cette mission

**Objectifs**

- en base de données
  - migrer toutes les propriétés secondaires dans les OCA
    - dans la bd les objets sont souvent en relation avec plusieurs autres objets donc nous avons des tables de jointure
    - ainsi sauf quelques exceptions qui ont été refactorées, il était trivial de déplacer les données et idem dans le code
    - dans l'autre cas
  - fusionner toutes les tables d'objet métier dans une seule avec la colone type en plus
  - fusionner tous les OCA en une seule table, aucun autre changement à faire
- dans le code
  - créer un type générique object avec un oca generic object dont étendent tous les objets métier
  - créer le generic object service avec toutes les méthodes communes des objets métier avec oca, une partie du code était dédoublée avec des erreurs de copier-coller donc erreurs en moins
  - mapper les classes avec Hibernate, discriminator value, sauvegarde oca cascade
  - minimisation des appels à la base de données
- dans le Front-End : rien, c'est tout l'idée
  - mais évolution du dev : écran générique de création / édition de tout et n'importe quoi

**Avantages**

Dans les URL nous utilisons souvent les identifiants d'objet métier, avec le nouveau sysyèmes ils sont tous uniques et il est posible de retrouver le type d'un objet à partir de son identifiant, ça répond à un besoin que nous avons

## Conclusion

Mon ressenti sur cette année d'alternance est très positif. J'ai pu approfondir mes connaissances en Java, en algorithmie, en bases de données et en toutes sortes de technologies du web. Les différentes missions que j'ai réalisées m'ont aidé à mieux comprendre le contenu de plusieurs de mes cours, et inversement.

J'ai également appris de nombreuses bonnes pratiques. Au delà des technologies j’ai mis en place une démarche quotidienne de recherches, d’étude des documentations, de tests, de débogage et de travail d'équipe pour avancer dans mes tâches. Mon code est devenu plus facile à lire, mieux organisé et j’ai pris l’habitude de correctement documenter mon travail avec les outils à ma disposition.

Mon travail sur le projet Subvention m'a appris beaucoup sur la mise en place d'un nouveau produit, sur l'importance de la performance d'une application, de la pertinence des logs ou messages d'erreurs et sur ma capacité à réfléchir sur des algorithmes. J'ai plusieurs fois remis mon travail en question et nous avons parfois dû annuler des missions qui n'ont pas eu le résultat prévu. Nous sommes une startup dont les outils évoluent très vite, il ne faut pas se laisser abattre à cause de quelques échecs.

Prochainement je vais commencer à travailler sur un nouveau produit de recherche de financements. Ce projet devrait être au moins aussi intéressant que le projet Subvention. Je vais donc continuer à travailler sur la création et l'amélioration des applications de Finalgo.

---

## Annexes

```sql
insert into OCA_PROJECT (id, object_attribute, 
object_id, object_key, object_value)
    select null, 'project_selected_company_id', id, -1,
   selected_company_id from PROJET;
```

*Migration vers les OCA*
