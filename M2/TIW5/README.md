# Rapport projet

À la suite des présentations chaque étudiant.e rédige un rapport de 6 à 10 pages
Le rapport contient une synthèse de chacun des thèmes présentés (y compris le thème auquel l’étudiant.e a participé)

<div style="clear:both;page-break-after:always;"></div>

## 1. Prise de décisions, arbitrage, gestion des conflits

blablabla

<div style="clear:both;page-break-after:always;"></div>

## 2. Gestion de la dette technique

blablabla

<div style="clear:both;page-break-after:always;"></div>

## 3. Qualité, adéquation du produit avec la demande

### Analyse fonctionnelle

Analyse du besoin : cadre
le cadre a un impact important sur la qualité produit

Adéquation du produit : validation
il faut répondre aux besoins du client : il doit valider

### Qualité fonctionnelle

faire des diagrammes pour exprimer le besoin et aiguiller les développeurs : doivent être compréhensibles par le client, pouvoir garder du recul

Organisation du travail
le client est très présent -> méthodes agiles qui maximise le ciblage des besoins clients
le client est peu présent ou la documentation est vraiment très précise -> cycle en V

Suivi de qualité
système de "tickets" qui permet de suivre chaque fonctionnalité, avoir un historique, définir les priorités, gérer les échéances

Processus de qualité
env de dev, preprod, prod

Tests
méthodes, procédures auto ou manu
par les développeurs ou les utilisateurs

Risques
on sous-estime le temps des tests, les impacts du passage de dev à preprod

Facteurs extérieurs
erreur sur la source de données de tests

### Qualité technique

Minimisation de la dette technique

versionning, réutilisabilité des composants, commentaires dans le code

Design patterns

Tests unitaires, analyse du code, couverture, ça met du temps à faire, donne retour/estimation qualité du code
l'intégration continue est un bon moyen d'automatiser ça, ça demande beaucoup de temps de configuration -> donc on fait pas sur petits projets, bloquer mise en prod si couverture de tests < pourcentage

Revue de code par exemple dans les méthodes agiles

Performances
il faut vérifier que ça ne baisse pas, il faut utiliser les outils chez soit et aussi chez la concurence pour comparer

<div style="clear:both;page-break-after:always;"></div>

## 4. Conception, propositions commerciales, chiffrage

Les dev s'en rendent pas compte, les commerciaux survendent les trucs, chaque entreprise a ± sa méthode mais 

Proposition commerciale : le commercial fait comprendre au client qu'il a compris son besoin, liste les services proposés, discute -> c'est mieux qu'un simple devis qui est similaire à une grille tarrifaire, c'est personnalisé, sur les salons commerciaux

Étapes exemple : appel téléphonique du commercial au client pour demander les besoins (procreption???), ça marche beaucoup mieux quand les entreprises sont dans le même secteur d'activité, les premières secondes de l'appel sont les plus importantes, taux d'acceptation, filtre des prestataires pour choisir lequel fera la prestation

Chiffrage : estimation datée du coup humain et matériel (information la plus importante des propositions commerciales), un chiffrage juste permet d'augmenter la crédibilité de l'entreprise
Astuce : tout prendre en compte chez le client (ses besoins), être ± honnête (mentir = pour gagner un gros client), dire ce qu'on fait et ce qu'on ne fait pas, parler de son expérience car c'est elle qui donne les meilleurs estimations, sinon la méthode de PERT qui prend en compte l'estimation optimiste, la probable pondérée à 4 et la pessimiste -> c'est assez efficace, il faut toujours utiliser la même méthode de chiffrage pour rester cohérent, il peut y avoir plusieurs chiffrage parfois tout au long d'un projet pour estimer le besoin, il faut identifier les différents corps de métier car non facturés pareil, toute l'équipe du projet peut y participer + les commerciaux, dans certains cas les tarifs sont fixes, le chiffrage est aussi adapté au budget du client
chiffrage en jour homme, en fonctionnalité

Conception : première phase dans le cycle de vie d'une initiative, définir les objectifs, l'organisation, identifier les risques et les contraintes pour ne pas tomber dans des cas irréversibles, bien identifier qui doit faire quoi, mettre en place un système de suivie (Gant, PERT, Organigramme) et avoir des solutions de repli en cas de problème (retard livraison, prestateur annulé) on peut le voir comme des panneaux sur une route, on peut se déplacer sur place et discuter avec les employés pour comprendre les attentes, retour sprint -> évolution du cahier des charges : on a une vision globale mais il y a toujours des évolution sur ce qui est fait

<div style="clear:both;page-break-after:always;"></div>

## 5. Gestion des coûts et des délais pendant la durée de vie du projet

Évaluer le cout des technologies, des personnels, des sous-traitants

Annalyse personnelle : il faut répartir le travail, les tâches, idéalement plusieurs personnes maitrisent les outils/technos

Coûts et délais : Sommes engagées pour le projet -> budget global, ensuite il faut savoir que tous les fonds ne sont pas dispo dès le début donc prévoir le système de paiement à certaines dates, selon le temps on va faire l'impasse ou non sur la qualité (triangle de d'or), minimiser les risques par l'analyse

Cycle de gestion des couts et delais : on réitere les étapes jusqu'à ce que le projet soit terminé

Gestion des couts : prendre en compte le prix de chaque coeur de métier, ajuster au budget, considérer ce qui a été payé ou qui va l'etre rapidement

Gestion des délais : on commence par une part de planification, il y a des outils dédiés comme msproject pour les diagrammes de Gantt, il faut pouvoir estimer qui fait quoi pendant combien de temps et dans quel ordre faire les choses pour bien estimer l'orga et minimiser l'impact des imprévus qui arriveront quoiqu'il arrive, les délais sont extrêmement importants surtout en cas de besoin éphémère, il faut avoir des méthodes de travail pour améliorer les connaissances des employés pour limiter l'impact des départs imprévus
Mise en place de systèmes de tickets avec estimation du temps, voir selon l'importance des livraisons ce qu'on peut changer pour respecter les déais avec les imprévus

Analyse : personne fait pareil, la théorie n'est pas appliquée en pratique même si on la connais, pas forcément le temps d'améliorer les processus, les clients ont des préférences sur les méthodes (agile, V) ou logiciels de monitoring, les clients n'ont pas de recul et concrètement ne savent pas ce qu'ils veulent (c'est flou) donc on doit passer plus de temps avec le client. Les différences de méthode n'impactent pas forcément la performance de l'entreprise à les appliquer efficacement pour le même résultat, c'est un grans système cout délai qualité, le processus d'amélioration de la gestion doit plutôt se faire en amont, l'agilité c'est bien avec les clients qui savent ce qu'ils veulent sinon le V c'est mieux

<div style="clear:both;page-break-after:always;"></div>

## 6. Agilité

Un CRM sert à gérer et optimiser les relations clients : gestion contact (fiches clients avec les données), gestion commerciale, automatisation de tâches type mail, module projet, dashboard personnalisés

Les méthodes agiles sont tirés du manifeste agile de 2001 qui ont estimé que les méthodes traditionnelles ne répondaient plus au besoin actuel qui évolue en permanence, ça s'adapte plus aux individus plutôt qu'aux contrats

SCRUM est une implémentation de ça avec un système d'itérations de 2 à 4 semaines où le product owner est en étroite collaboration avec l'équipe

Pilotage : analysse des besoins et planifications
En V tout sera planifié en amont alors qu'en agile la planification n'est que sur la prochaine itération, on liste ± toutes les user stories et établi les étapes de développement, toutes les parties participent aux itérations, le PO va attribuer les user stories du sprint

Dans l'exemple du bureau d'étude on retrouve des aspects de la méthode agile

On peut avoir des micro cycles en V de quelques mois

Sprint planning, sprint poker
Les user stories, plus le projet avance plus elles deviennent précises ex. mot de passe oublié. Les US se voient affecter des tâches

Déroulement d'un sprint : on commence par une réunion quotidienne où on dit ce qu'on a fait la veille, ce qu'on va faire le jour et les difficultés qu'on a rencontré. ça permet à l'équipe de se synchoniser

Sprint burndown : outil de visualisation qui doit être mis à jour après chaque daily pour voir où en est l'avancement par rapport à la prévision (30 points / semaine par exemple)

Démonstration client : cycle en v rien, méthodes agiles on montre ce qui a été fait lors de la dernière itération

Revue de sprint : cycle en v rien, chacun présente ce qu'il a fait et tout le monde peut faire des retours

Rétrospective scrum : réunion qui permet de lister ce qui s'est bien passé, mal passé et ce qui peut être amélioré. Le but est de faire une synthèse de ce qu'il faut continuer et de ce qu'il ne faut plus faire

Livraison produit : agile factionné, mep après chaque fonctionnalité, test du système en continue, en v on attend la toute fin pour mep et tester

bilan les méthodes agiles sont plus réactives pour s'adapter aux changements nécessaires
