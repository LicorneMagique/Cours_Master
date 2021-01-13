# Rapport alternant

## Page de garde

## Table des matières

- Présentation de Finalgo
  - L'équipe
  - Les projets
- Gestion des projets
  - Organigramme Scrum
  - Rôles
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

## Présentation de Finalgo

Finalgo est une startup spécialisée dans la recherche de financements, la construction et la gestion de dossiers de financement.

Finalgo est la première solution 100% digitale de recherche de financement. Elle permet à tous les dirigeants d’entreprise de construire et d’envoyer eux-même leurs dossiers de financements à tous types de partenaires financiers. www.finalgo.fr

Notre vocation :
Faciliter l'accès au financement pour les entrepreneurs, artisans, commerçants, dirigeants de TPE / PME
Mettre le numérique au service de l'humain.
Le financement est le carburant de l'entreprise, libérons le !

### L'équipe

À Finalgo la hiérarchie est complètement horizontale, l'organigramme est donc organisé suivant le type du poste.

*image ici*

- Les cofondateurs
  - Bertrand HELLION (directeur technique)
  - Arnaud GUILLAUME (directeur général)
- Les salariés
  - Jade ABERBOUR (développeur)
  - Valentin MEREAU (développeur)
- Les alternants
  - Célia BERTHELIER (assistante communication)
  - Julien GIRAUD (développeur)
  - Paul JUYAUX (développeur)

### Les projets

*Rappeler les projets auxquels vous participez*

Je participe au développement de trois projets, **Main** notre application principale, **crossroads** notre produit dirrigeant (idéalement l'avenir de Finalgo) et **finsearch** une sorte de Main simplifié dont nous gérons le développement et la maintenance pour l'un de nos clients.

En terme de code chaque application possède un front Angular et un back Java Spring qui fonctionne sous forme d'une API REST. Le back est le même pour Main et pour Crossroads, puis Finsearch possède un front et un back ce qui nous fait 5 projets.

*un petit schéma plutôt que ce tableau*

| Front Angular | Back Java Spring |
| ------------- | ---------------- |
| Main | Main |
| Main | Crossroads |
| Finsearch | Finsearch

## Gestion des projets

### Organigramme Scrum

À Finalgo nous fonctionnons au maximum suivant la méthode Scrum.

![.](https://www.mendix.com/wp-content/uploads/scrum-team.png)

- Bertrand HELLION (Product owner | Développeur full stack)
- Jade ABERBOUR (Scrum master | Développeur front)
- Valentin MEREAU (Développeur full stack)
- Julien GIRAUD (Développeur full stack)
- Paul JUYAUX (Développeur full stack)

### Notre échelle de difficulté des tâches

| Nombre de points | Difficulté | Lignes de code | Temps de travail |
| ---------------- | ---------- | -------------- | ---------------- |
| 1 | Vraiment très facile | 1 à 10 | Une dizaine de minutes |
| 2 | Nous utilisons la suite de Fibonacci donc en théorie le `2` est possible mais nous ne l'utilisons jamais car il est trop proche du `1` |
| 3 | Facile | 5 à 30 | Une heure ou deux |
| 5 | Moyenne | 20 à 100 | Une demie journée |
| 8 | Difficile | 30 à 500 | Un jour ou deux |
| 13 | Très difficile | 50 à 2000 | Environ une semaine |
| 21 | Impossible, on estime que c'est la difficulté d'un projet entier. `21` signifie qu'il faut découper la tâche en une liste de sous-tâches | ∞ | Entre 6 mois et un millénaire |

\* Pour un même niveau de difficulté il y a en général beaucoup de lignes sur les tâches purement front et peu sur les tâches d'algorithmie ou de code métier.

### Rôles

*Bertrand : il me donne du boulot quand j'ai plus rien à faire, il m'explique le code quand je comprends pas ce qu'il a fait et il review la segfaultativité de mes algos, souvent il m'appelle pour avoir des conseils sur les bonnes pratiques de code ou des suptilités de TypeScript*  
Bertrand joue à la fois le rôle de Product Owner et de développeur.
En tant que Product Owner il s'occupe de comprendre et lister les besoins de nos clients (Business Owner) afin de créer une liste tâches. Il essaie également de les rendre indépendantes dans la façon de les écrire pour permettre une bonne répartition au sein de l'équipe.  
En tant que développeur (et Docteur en recherche opérationnelle) il s'occupe d'assigner les points de difficulté aux tâches en rapport avec le back ou le code métier du front, et il s'occupe de certaines de ces tâches.

*Jade : elle anime le goûter, quand j'ai de l'affichage à faire je vois ça avec elle, quand elle craque parce que Bertrand fait des bêtises parfois je l'aide
Jade occupe le double rôle de Scum Master et de développeur front.*
En tant que Scrum Master elle paticipe aux réunions clients avec Bertrand où elle s'occupe des démonstrations et elle gère les parties UX/UI en tant que graphiste de formation. Elle s'occupe aussi d'animer les réunions quotidiennes et d'organiser des sorties Team Building.  
En tant que développeur front et graphiste elle s'occupe de donner les points d'effort aux tâches purement front, elle participe activement à leur développement et elle design des maquêtes d'interfaces qui nous permettent de visualiser les User Stories.

Valentin : globalement on fait les mêmes choses sauf qu'il touche trois fois mon salaire, c'est un professionnel d'Angular et il touche son pied sur ce qui est config serveur donc quand je suis bloqué sur ce genre de choses je lui demande. Il s'occupe aussi de mes PR vu que c'est le seul qui comprend ce que je fais ET qui teste mon code

Paul : il fait à peu près pareil que moi mais sur d'autres projets, on a jamais trop travaillé ensemble mais parfois on se fait des code review

Arnaud : il joue le rôle d'intermédiaire avec Finsearch (par exemple quand j'ai besoin du mot de passe de leur compte Stripe...), il trouve pleins de bugs sur Main et nous demande de les corriger, il a pleins d'idées d'amélioration de Main et il essaie de nous les faire développer, il a pleins d'idées pour ce qu'on peut faire avec Crossroads (l'avenir de Finalgo, on l'espère) et je me retrouve à les dev
SME (Subject Matter Expert) en tant qu'ex expert comptable ET Business Owner de main en tant qu'utilisateur de l'application
