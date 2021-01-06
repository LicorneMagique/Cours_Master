# Rapport alternant

## Consignes

Rédiger un petit rapport sur l’**organisation** et la **gestion des projets** au sein de votre entreprise

Ce rapport est à déposer sur Tomuss (case "Rapport alternant" de l’UE UE-INF1096M Projet Transversal De Master Informatique) pour le **24/01**

Il est conseillé de commencer dès maintenant à travailler sur ce document et d’envisager de le rendre en avance, par exemple à la rentrée (autour du **04/01**) pour ne pas être débordé en janvier

### Contenu

- Rappeler les **projets** auxquels vous participez
- Décrire l’**équipe** à laquelle vous êtes intégré (**organigramme**)
- Préciser le **rôle** des personnes avec qui vous interagissez OU qui ont un impact sur votre travail
- Décrire la manière dont sont **gérés les projets** auxquels vous participez
  - Faire le lien avec la pratique d’une ou plusieurs méthodologies vue en cours en **génie logiciel**
- Décrire quelles démarches spécifiques au **travail à distance** ont été mises en place
  - Qu'est-ce qui fonctionne ?
  - Qu'est-ce qui ne fonctionne pas et pourrait être amélioré ?

### Mise en forme

Il faut faire un effort de synthèse

- Réfléchissez aux informations que vous voulez communiquer
- Soinez votre document
  - Vérifiez l’**orthographe** et la **grammaire**
  - Reprenez un **modèle de document interne** à votre entreprise
- Environ **5 pages** hors **page de garde** et **table des matières**

N’hésitez pas à faire relire ce document avant de le déposer

## Rapport

### Page de garde

### Table des matières

- Finalgo
  - Activité
  - Projets
- Équipe
  - Organigramme
  - Rôles
- Gestion projets
  - Méthodologie
  - Outils
    - Slack
    - Asana
    - Meet
- Travail à distance
  - Café
  - Goûter
  - Asana
  - Meet
  - Slack

### Présentation de Finalgo

Finalgo est une startup spécialisée dans les applications web de recherche de financements "algorithmée" et la construction de dossiers de financement

Nous disposons de trois projets, **main** notre principale application, **crossroads** notre produit dirrigeant et **finsearch** une sorte de main simplifiée dont nous gérons le développement et la maintenance pour le client CEFIN.

Finalgo est la première solution 100% digitale de recherche de financement. Elle permet à tous les dirigeants d’entreprise de construire et d’envoyer eux-même leurs dossiers de financements à tous types de partenaires financiers. www.finalgo.fr

Notre vocation :
Faciliter l'accès au financement pour les entrepreneurs, artisans, commerçants, dirigeants de TPE / PME
Mettre le numérique au service de l'humain.
Le financement est le carburant de l'entreprise, libérons le !

### Présentation de l'équipe

#### Organigramme

À Finalgo la hiérarchie est complètement horizontale, l'organigramme sera donc organisé suivant le type du contrat.

- Les cofondateurs
  - Bertrand HELLION (directeur technique)
  - Arnaud GUILLAUME (directeur général)
- Les salariés
  - Jade ABERBOUR (développeur front end)
  - Valentin MEREAU (développeur full stack)
- Les alternants
  - Célia BERTHELIER (assistante communication)
  - Julien GIRAUD (développeur full stack)
  - Paul JUYAUX (développeur full stack)

#### Rôles de chacun

Bertrand : il me donne du boulot quand j'ai plus rien à faire, il m'explique le code quand je comprends pas ce qu'il a fait et il review la segfaultativité de mes algos, souvent il m'appelle pour avoir des conseils sur les bonnes pratiques de code ou des suptilités de TypeScript

Arnaud : il joue le rôle d'intermédiaire avec Finsearch (par exemple quand j'ai besoin du mot de passe de leur compte Stripe...), il trouve pleins de bugs sur main et nous demande de les corriger, il a pleins d'idées d'amélioration de main et il essaie de nous les faire développer, il a pleins d'idées pour ce qu'on peut faire avec Crossroads (l'avenir de Finalgo, on l'espère) et je me retrouve à les dev

Jade : elle anime le goûter, quand j'ai de l'affichage à faire je vois ça avec elle, quand elle craque parce que Bertrand fait des bêtises parfois je l'aide

Valentin : globalement on fait les mêmes choses sauf qu'il touche trois fois mon salaire, c'est un professionnel d'Angular et il touche son pied sur ce qui est config serveur donc quand je suis bloqué sur ce genre de choses je lui demande. Il s'occupe aussi de mes PR vu que c'est le seul qui comprend ce que je fais ET qui teste mon code

Célia : on sera peut-être amené à travailler ensemble sur le projet des subventions ou si elle a besoin d'installer des trucs de marketing sur main ou crossroads mais sinon pas trop

Paul : il fait à peu près pareil que moi mais sur d'autres projets, on a jamais trop travaillé ensemble mais parfois on se fait des code review

### Les projets

#### main back

Serveur de notre principale application

- Refacto code déprécié
- Renommage des PA
- Téléchargement dossier PED
- Dev note de synthèse / iText
- API insee
- API subvention
- Connexion SSO OpenID Cafpi
- MAJ du code antivirus
- Refactoring de quelques noms de classe en rapport avec la note de synthèse
- Ajout d'un système d'unité (mois, %, €, année(s)) dans les OCA (système de stockage ressemblant à du NoSQL)
- Implémentation d'un système générique pour la génération de la couverture des notes de synthèse avec du contenu dynamique, librairie IText
- Début du développement du système de connexion SSO avec Microsoft Azure pour l'un de nos clients
- Mise en place d'un système de connexion SSO / OpenID Connect sur notre application pour que les utilisateurs du client Cafpi puissent se connecter avec leur compte Microsoft Azure (back)

#### main front

Interface utilisateur de notre principale application

- Ajout du système d'unité des OCA sur les ITE (propagation du système d'unité dans le front)
- Début de l'implémentation de la connexion par SSO Microsoft Azure
- Mise en place d'un système de connexion SSO / OpenID Connect sur notre application pour que les utilisateurs du client Cafpi puissent se connecter avec leur compte Microsoft Azure (front)
- Mise en place du redémarrage et des mises à jour automatique du service antivirus sur notre serveur
- Mise en place d'un service Java permettant de manipuler l'API REST Open Data du site aides-entreprises.fr

#### crossroads

Interface du produit dirrigeant, idéalement l'avenir de Finalgo

- Refacto Stripe
- Dev subvention
- Refactoring du système de gestion des acticles Stripe pour quelque chose de plus générique et typé (permettant de détecter plus d'erreurs qu'avant)
- Réimplémentation de toute l'API Stripe avec la dernière version, l'ancienne version était complètement dépréciée

#### finsearch back

Serveur d'un projet secondaire

- Refactoring de quelques méthodes du projet (corrections de warnings)
- Corrections d'orthographe
- Refactoring de la gestion des fichiers de CGU envoyés en pièce jointe aux emails de confirmation d'inscription
- Implémentation de la persistance de la plateforme de connexion des utilisateurs et d'un système de mise à jour pour compléter la colone de cet attribut en BD
- Implémentation de la persistance de la plateforme de connexion des utilisateurs et d'un système de mise à jour pour compléter la colone de cet attribut en BD
- Google tag manager / analytics
- Refactoring de la gestion des fichiers de CGU envoyés en pièce jointe aux emails de confirmation d'inscription

#### finsearch front

Côté utilisateur (dont l'interface) du projet secondaire, il y a 5 plateformes différentes qui utilisent ce projet en parallèle

- Corrections de style (SCSS)
- Mise à jour du contenu
- Amélioration de l'UI
- Ajout d'une colone "plateforme source" dans le tableau administrateur pour trier les utilisateurs en fonction de ce paramètre

### Compétences en wrac

- Envoyer un mail et y attacher des pièces-jointes avec l'API Sendinblue
- Rajouter un attribut à une classe Java et le persister dans une base de données MySQL avec Hibernate
- Ajouter une colonne avec un système de filtre dans un tableau sur Angular
- Installer et utiliser l'antivirus ClamAV depuis une classe Java
- Générer des PDF avec un contenu dynamique en utilisant la librairie IText
- Implémenter un système générique de personnalisation de contenu à partir d'une liste de priorité
- Implémenter un système de connexion par SSO avec Microsoft Azure sur Angular
- Implémenter un système de connexion par SSO avec Microsoft Azure sur Java
- Implémenter un système générique à base d'énumérateur sur Angular pour typer des chaînes de caractère
- Implémenter l'API Stripe pour mettre en place un système de paiement sur un projet Angular
- Utiliser le librairie @microsoft/mgt pour mettre en place une connexion SSO avec Microsoft Azure sur un front Angular
- Récupérer la clé publique d'un JWT OpenID Connect
- Vérifier la validité d'un JWT
- Récupérer les informations contenues dans un JWT
- Créer un service Linux et configurer son démarrage automatique au chargement du système
- Effectuer des requêtes vers des API depuis un projet Java Spring Boot
- Manipuler les données de l'API aides-entreprises.fr
