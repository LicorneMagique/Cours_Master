# Rapport final d'alternance

Ce document est un brouillon du rapport final.

## Page de garde

Titre :

> Rapport final d'alternance  
> développeur full stack  
> chez Finalgo

Petit encadré sur les deux dernières lignes du titre ?

Bloc "réalisé par / tuteurs"

> Réalisé par : Julien Giraud  
> Diplôme préparé : Master 1 Informatique  
> Tuteur entreprise : Bertrand Héllion  
> Tuteur pédagogique : Marc Plantevit  
> Durée : du 07/09/2020 au 30/08/2021 (1 an)

## Remerciements

Je tiens à remercier Bertrand Hellion de m'avoir accepté à Finalgo et accompagné tout au long de l'année. Je remercie Marc Plantevit de m'avoir suivi et conseillé. Je remercie également toute l'équipe Finalgo ainsi que les trois dernières générations de stagiaires et alternants pour m'avoir accueilli, intégré et partagé leur bonne humeur.

## Table des matières

- [Rapport final d'alternance](#rapport-final-dalternance)
  - [Page de garde](#page-de-garde)
  - [Remerciements](#remerciements)
  - [Table des matières](#table-des-matières)
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
  - [Environnement technique](#environnement-technique)
    - [Côté serveur](#côté-serveur)
    - [Côté client](#côté-client)
    - [Outils de développement](#outils-de-développement)
  - [Missions effectuées](#missions-effectuées)
    - [Écran d'administration de Finsearch](#écran-dadministration-de-finsearch)
    - [Ajout de la connexion SSO sur Main et sur Crossroads](#ajout-de-la-connexion-sso-sur-main-et-sur-crossroads)
      - [SSO Microsoft Azure sur Main](#sso-microsoft-azure-sur-main)
  - [Conclusion](#conclusion)

## Introduction

Dans le cadre de ma premire année de Master Informatique à l'UCBL j'ai opté pour un cursus en alternance au sein de Finalgo, une startup locale spécialisée dans les applications web en lien avec les financements.

J'ai pu effectuer cette alternance suite à mon stage optionnel de L3 réalisé au même endroit. Pour celle-ci, un contrat d'apprentissage de deux ans a été signé. Cette période correspond à un Master qui se termine par un diplôme dans les Technologies de l'Information et Web (TIW).

Les notions vues en cours lors de mon DUT et de ma Licence ainsi que mes précédentes expériences professionnelles m'ont beaucoup aidé à réaliser mes missions en entreprise.

Certaines missions ont renforcé mes connaissances, d'autres m'ont permi de comprendre des éléments abordés au cours de l'année dans un vrai cadre professionnel.

Tout au long de l'année j'ai réalisé des missions diverses sur l'ensemble des applications de Finalgo.

## Présentation de Finalgo

Finalgo est une startup familiale de 6 collaborateurs spécialisée dans

- la recherche de financements 100 % digitale,
- la construction et la gestion de dossiers de financement,
- la recherche de subventions.

Nous proposons à nos clients des outils qui permettent de répondre à ces besoins. Ces outils sont des applications web avec un système d'abonnement payant, il s'agit du modèle d'exploitation commerciale « SaaS » pour « Software as a Service ». Notre objetif est de leur permettre de construire et d’envoyer eux-même leurs dossiers de financements à tous types de partenaires financiers, ou de trouver les aides éligibles pour leur entreprise.

Notre vocation est de faciliter l'accès au financement pour les entrepreneurs, artisans, commerçants et plus généralement aux dirigeants de TPE / PME.

### L'équipe

À Finalgo la hiérarchie est complètement horizontale, pour chaque tâche le référent est la personne qui maîtrise le mieux la partie métier ou technique correspondante. L'organigramme est donc organisé suivant le type du contrat.

![organigramme](./assets/organigramme.svg)

\* Non présents en même temps

### Les projets

Cette année j'ai participé au développement des quatre projets principaux de Finalgo,

- **Main** notre application de construction et de gestion de dossiers de financement,
- **Crossroads Financing** notre application de recherche de financements,
- **Crossroads Subvention** notre application de recherche de subventions,
- **Finsearch** une sorte de Main simplifié dont nous gérons le développement et la maintenance pour l'un de nos clients.

En terme de projets informatiques, chaque application possède un front\* Angular\* et un back\* Java Spring Boot\* qui fonctionne sous forme d'une API REST\*. Le back est le même pour Main et pour Crossroads, Finsearch possède un front et un back. Il y a également un petit serveur Python\* Flask\* qui communique avec le back de Main, ce qui fait au total 6 projets informatiques différents.

![projets](./assets/projets.svg)

## Environnement de travail

### Matériel et lieu

À Finalgo nous travaillons beaucoup en télétravail. Lorsque nous allons dans les locaux, en général une fois par semaine pour les membres de l'équipe qui sont à proximité de Lyon, nous allons au HUB612. Il s'agit d'un incubateur, une sorte d'open space avec une équipe qui accompagne les entreprises. Le HUB612 est spécialisé dans les entreprises qui travaillent sur la finance, les assurances et le marketing à l'aide d'outils numériques modernes. C'est un lieu agréable pour travailler et échanger avec des personnes dans des domaines similaires aux nôtres.

Pour travailler on a mis à ma disposition un ordinateur portable avec une très bonne configuration, ce qui me permet d'utiliser efficacement tous les logiciels dont j'ai besoin. J'utilise généralement un deuxième écran pour des questions de confort, il y en a sur les bureaux du HUB* et j'utilise mon écran personnel en télétravail.

### Outils et logiciels

Depuis le début de la crise sanitaire, toute notre organisation est basée sur du travail en distanciel. Nous sommes donc équipés en outils de communication, visioconférence, gestion des tâches et suite de bureautique.

#### Slack

<img alt="slack" src="./assets/slack.svg" width="64"> Slack est notre outil de communication n°1 interne comme externe.

<img alt="slack" src="./assets/channels.png" width="90" style="float: left; margin-right: 3em">

En **interne** nous avons un espace de travail "Finalgo" avec des **canaux de discussion** pour tous les sujets, ce qui permet de configurer les notifications qu'on souhaite recevoir pour chaque type d'information.

Il y a un canal pour

- chaque **projet** : Main, Crossroads
- chaque **domaine** : informatique, marketing, communication, design, recrutement, teambuilding…
- chaque **type de logs** : bugs utilisateurs, boutons "demander de l'aide", actions utilisateurs, actions nécesitant une intervention de notre part, traces des différents serveurs de production et de développement…
- la **détente** : on y trouve des blagues ou liens en tout genre pour partager de la bonne humeur avec l'équipe.

En **externe** nous avons un espace de travail pour chaque client, au sens entreprise qui utilise l'une de nos applications et qui a demandé un développement spécifique.

#### Asana

<img alt="asana" src="./assets/asana.svg" width="64"> Asana est notre plateforme de gestion des tâches.

La plateforme permet de créer des projets qui fonctionnent comme les tableaux sur
Trello. Il est possible d'y créer des colonnes et d'y ajouter des tâches avec des attributions, des images, des sous-tâches.

Nous utilisons ces tableaux pour remplacer le **Scrum Board**, un tableau de post-it utilisé par la méthode SCRUM qui est à l'origine de notre méthode de travail. Grâce à ces tableaux nous pouvons voir qui travail sur une tâche, connaître son avancement, en ajouter nous-même et écrire les spécification. Il y a beaucoup plus de fonctionnalités sur le site mais nous ne les utilisons pas pour le moment.

#### Google Workspace

<img alt="gmail" src="./assets/gmail.svg" width="64"> | <img alt="drive" src="./assets/drive.svg" width="64"> | <img alt="meet" src="./assets/meet.svg" width="64"> | <img alt="calendar" src="./assets/calendar.svg" width="64"> | <img alt="sites" src="./assets/sites.svg" width="48"> | <img alt="sheets" src="./assets/sheets.svg" width="48"> |
| ----- | ----- | ---- | -------- | ----- | ------ |
| Gmail | Drive | Meet | Calendar | Sites | Sheets |

Finalgo utilise un système de comptes Google pour les entreprises. Nos comptes nous permettent d'accéder à la suite de bureautique comme avec une adresse **Gmail** classique, même s'ils terminent par `@finalgo.fr`. Toutes ces applications sont liées à un espace partagé sur **Google Drive**, auquel nous avons tous accès avec notre compte.

**Meet** est une plateforme de réunions numériques très simple à utiliser. Il est possible de se connecter à un salon grâce à un lien, on peut ensuite participer avec sa caméra, son micro ou en faisant des partages d'écran. Nous passons beaucoup de temps sur Meet, surtout pour parler avec l'équipe mais aussi pour les réunions clients.

**Calendar** est un agenda, il sert surtout à planifier des rendez-vous clients ou des points d'équipe importants. Un salon meet est associé à chaque événement de l'agenda. Ce système évite de générer un lien et de l'envoyer aux invités, il suffit de les ajouter sur un événement.

**Google Sites** sert exclusivement à voir et alimenter notre wiki interne. Il s'agit d'un site accessible uniquement avec notre compte, sur lequel nous répertorions toutes sortes d'informations utiles pour Finalgo. On y trouve les procédures comme les mises en production, les installations, les plateformes et il y a des explications sur les technologie inhabituelles. C'est un outil que nous utilisons et alimentons beaucoup, il entre dans la philosophie SCRUM en facilitant les formations mutuelles au sein de l'équipe.

**Sheets** est un tableur comme Excel, nous l'utilisons en interne et en externe. Il y a des tableaux administratifs pour gérer des choses comme les congés, certains servent d'outils de maintenance et ticketing, d'autres permettent de synthétiser des informations afin de les exporter dans le code.

## Environnement technique

### Côté serveur

Pour les serveurs nous avons un compte sur la plateforme OVH avec une dizaine de VPS (virtual private server) sous Debian.

Sur ces VPS nous avons un serveur Apache pour servir le front compilé par Angular et un serveur Tomcat pour le back Java Spring Boot.

Dans le cadre de Main il y a aussi un serveur Flask sur Python 3.8.

Nos projets Spring Boot utilisent Java version 11 avec divers dépendances. Voici un résumé des plus utilisées et de celles que j'ai utilisées.

| Dépendance | Description |
| ---------- | ----------- |
| Auth0 | Librairie qui permet de manipuler les JWT. |
| ClamAV | Librairie qui permet de communiquer avec le logiciel ClamAV installé sur la machine. |
| Hibernate / HQL | Framework qui permet de manipuler la base de données à travers des interfaces. Il implémente le HQL, un langage de requête de base de données relationnelles similaire à SQL avec une approche orientée objet. |
| Itextpdf | Librairie payante qui permet de manipuler les PDF et d'en générer à partir de code HTML. |
| Sendinblue | Librairie qui permet de communiquer avec l'API de Sendinblue, un service web d'envoi d'email orienté marketing. |
| Stripe | Librairie qui permet de communiquer avec l'API de Stripe, un service web de paiement en ligne. |
| Swagger | Une interface qui permet de visualiser l'architectures d'une API et d'y envoyer des requêtes. |

Il y a d'autres programmes installés sur les serveurs, les plus importants sont les suivants.

ClamAV : logiciel antivirus open source compatible Linux et MacOS.

Mysql : système de gestion de bases de données relationnelles.

Python : langage de programmation orienté objet de haut niveau.

Cron : programme qui permet de programmer l'exécution de scripts ou de logiciels sur Linux.

### Côté client

En front nous utilisons Angular 11, un framework open source de Google basé sur le langage TypeScript. Le code HTML Angular utilise une syntaxe enrichie par rapport au HTML5, il est possible d'y insérer des éléments de code. Il y a également une prise en charge du langage Saas qui permet de simplifier la syntaxe du CSS. Nous utilisons la version SCSS de Saas car sa syntaxe inclue celle du CSS.

TypeScript est un langage de programmation libre et open source de Microsoft. Ce langage est basé sur Javascript avec un système de typage, de classes et d'éritage similaire à celui de Java. Il est possible de convertir du code TypeScript en code Javascript.

Notre projet Angular utilise divers dépendances. Voici un résumé des plus utilisées.

| Dépendance | Description |
| ---------- | ----------- |
| Bootstrap | Ensemble de classes CSS qui permettent de simplifier la mise en place du responsive design. |
| Forms | Ensemble de Classes et composants Angular qui permettent de gérer les formulaires. |
| HelpHero | Librairie qui permet de créer des product tour à partir d'une interface web. |
| Material | Ensemble de classes et composants Angular qui permettent de créer des interfaces graphiques d'application très facilement. |
| Router | Ensemble de classes et composants Angular qui permettent de gérer les routes d'une application et de manipuler l'URL. |
| SweetAlert2 | Librairie qui permet d'afficher toutes sortes de pop-up personalisables. |

### Outils de développement

De façon générale il y a beaucoup d'informations utiles pour le développement sur notre wiki. On y trouve notamment :

mettre exemple page wiki annexe

- les commandes à utiliser pour installer MySQL sur notre machine et y charger une copie de la base de données de production,
- la procédure à suivre pour tester le paiement par Stripe depuis notre environnement de développement local,
- la procédure à suivre pour faire une mise en production du back ou du front,
- les commandes à utiliser pour récupérer les logs des différentes applications de la production.

Pour développer en front j'utilise Visual Studio Code comme IDE. Il s'agit d'un éditeur de code sur lequel on peut ajouter divers extensions pour simplifier le développement, notamment sur Angular. J'utilise également beaucoup les outils de développement de Google Chrome, dont le débugger permet de suivre l'éxécution du code TypeScript.

Pour le back j'utilise l'IDE IntelliJ qui est très efficace pour le Java. J'utilise beaucoup le débugger de cet IDE, à la fois pour visualiser l'exécution du code ligne par ligne mais aussi pour tester en direct du code Java.

Ajouter 2 annexes pour le débugger intellij

Lorsque nous avons besoin d'accéder aux derniers logs d'une application possiblement en production nous pouvons directement utiliser les channels Slack correspondants à chacun des types de logs. Nous en avons une douzaine au total, il y en a un pour :

- chaque serveur tomcat de production comme de développement (Ti),
- la totalité des logs (Ti,1),
- toutes les actions utilisateur (Ti,2)
- tout ce qui nécessite notre intervention (Ti,3).

Pour tous nos projets nous utilisons GIT comme gestionnaire de version et le code est sauvegardé en ligne sur GitHub. Nous avons tous un compte sur cette plateforme et nous avons les droits d'accès sur les différents projets, par défaut ils sont inaccessibles.  
Pour gérer les commits et les branches j'utilise une extension de Visual Studio Code qui propose une excellente interface graphique. Cette interface permet d'effectuer toute sorte d'opération très facilement, en particulier de ne commiter que certaines lignes de code dans un fichier ou de visualiser les différences entre les commits.

Mettre dans annexe

![git_log](./assets/git_log.png)
![git_code](./assets/git_code.png)

Enfin pour travailler sur les bases de données nous utilisons DBeaver, un logiciel libre avec une interface plutôt intuitive.

![dbeaver](./assets/dbeaver.png)

## Missions effectuées

### Écran d'administration de Finsearch

Le projet Finsearch était en plein développement lorsque je suis arrivé à Finalgo. L'une de mes premières missions était de réaliser l'écran d'administration des projets pour le personnel de Cefin, l'entreprise à l'origine du projet Finsearch. Cet écran permet aux administrateurs de voir tous les dossiers en cours de traitement par l'application, avec divers informations sur chaque dossier.

En front l'écran n'est accessible pour les utilisateurs administrateurs. Il affiche un tableau dont chaque ligne récapitule l'avancement d'un utilisateur dans la gestion de son plan de financement, voir annexe. Il est possible de trier le tableau à partir de ses colonnes et l'administrateur peut se connecter sur le compte d'un utilisateur pour voir son dossier à partir de sa ligne dans le tableau, voir annexe.

annexes ![finsearch](./assets/finsearch.png) ![finsearch_popup](assets/finsearch_popup.png)

En back il a fallu récupérer les différentes informations à afficher. Certaines étaient liées à l'utilisateur, d'autres aux projets de cet utilisateur. Il y a un traitement pour ne récupérer que les informations les plus importantes afin de n'afficher qu'une ligne par utilisateur.

Cet écran était la dernière étape pour le projet Finsearch soit utilisable par Cefin.

### Ajout de la connexion SSO sur Main et sur Crossroads

Dans le cadre d'un développement spécifique de Main et de l'amélioration des produits Crossroads, je me suis occupé de toutes les tâches relatives au Single Sign-On aussi souvent appelé SSO. Il s'agit de la technologie à l'origine des boutons *Se connecter avec Google ou Facebook*. L'objectif de ces tâches est donc de permettre aux utilisateurs de se connecter sur nos plateformes à partir de leurs comptes déjà existants sur
d'autres plateformes, en l'occurence Google ou Microsoft.

Personne n'avait développé ce type de fonctionnalité dans les projets de Finalgo, je me suis donc chargé d'écrire la page SSO sur notre wiki interne pour expliquer son fonctionnement et lister les liens utiles.

Afin de mieux comprendre le processus de connexion il faut savoir que pour être connecté, notre front doit avoir récupérer l'utilisateur courrant ainsi qu'un JWT valide depuis notre back.

#### SSO Microsoft Azure sur Main

J'ai commencé par implémenter une connexion SSO sur Main dans le cadre d'un développement spécifique pour notre client Cafpi. Leur entreprise utilise la suite Microsoft Azure qui permet la mise en place du SSO pour ses utilisateurs.

Dans le cadre de cette tâche tous les comptes existaient déjà sur Main, autrement dit la question de la création de compte ne se posait pas. Le travail à réaliser était d'ajouter une page de connexion qui se charge de récupérer un JWT Microsoft Azure, puis qui s'en serve pour récupérer l'utilisateur et un JWT Finalgo auprès du back afin de connecter l'utilisateur. En back il fallait donc être capable de vérifier ce nouveau type de JWT.

![sso](./assets/sso.png)

Pour le front Microsoft fournit une librairie qui permet de gérer le processus de connexion SSO, c'est à dire la redirection vers le site où se connecte l'utilisateur et la récupération du JWT suite à cette connexion. Il suffit de fournir divers identifiants de configuration à la librairie et elle se charge de nous retourner le JWT.

En back il n'était pas possible d'utiliser les librairies de SSO pour des raisons de conflit avec le système de connexion normal. Le plus simple était de faire une vérification manuelle. Pour ce faire il faut récupérer la clé publique du JWT sur l'API de Microsoft afin de vérifier la signature. Le problème se complique car il y a plusieurs clés sur l'API en question, afin d'identifier la bonne clé il faut utiliser un code appelé identifiant du token ou kid, ce code se trouve à l'intérieur du JWT. Une fois la clé récupérée il faut effectuer divers conversions avant de finalement vérifier la signature du JWT, ce qui équivaut à vérifier sa validité.

![jwt](./assets/jwt.png)

> <https://nordicapis.com/why-cant-i-just-send-jwts-without-oauth/>

## Conclusion
