# Rapport projet

À la suite des présentations chaque étudiant.e rédige un rapport de 6 à 10 pages
Le rapport contient une synthèse de chacun des thèmes présentés (y compris le thème auquel l’étudiant.e a participé)

<div style="clear:both;page-break-after:always;"></div>

## 1. Prise de décisions, arbitrage, gestion des conflits

### Qu'est-ce que la prise de décisions ?

La prise de décision a pour objectif de répondre à une question décisionnelle en se basant sur un ensemble de contraintes liées au problème. On distingue en particulier trois types de problèmes en entreprise, techniques, humains et stratégiques.

Les **problèmes techniques** sont liés à des contraintes pragmatiques comme le temps disponible, le coût, l'architecture ou les implémentations. Il faut prendre en compte des notions comme l'intéropérabilité', le passage à l'échelle ou les qualifications des équipes. On résout généralement ce type de problème par le biais de recherches, d'expérimentations et d'outils de monitoring.

Les **problèmes humains** sont axés sur la gestion du personnel, du point de vue du recrutement ou des équipes. L'objectif est d'obtenir une meilleure productivité. Les méthodes de doivent être adaptées en fonction des besoins et des effectifs, avec des méthodes agiles ou plus classiques comme les cycles en V. Les formations internes permettent également de résoudre des problèmes au niveau des individus.

Les **problèmes stratégiques** sont plus généraux, ils aussi pour but d'augmenter la productivité et la réactivité mais peuvent s'appliquer à d'autres domaines. On les traite surtout via des réunions et des méthodes de réflexion comme le brainstorming.

### Les contraintes

La prise de décision est fortement influencée par des contraintes. Il existe des contraintes internes sur lesquelles nous pouvons potentiellement agir, et des contraintes externes que nous sommes généralement obligé de subir. Dans tous les cas, ces contraintes ont un impact sur la prise de décision.

En contrainte interne il y a par exemple le temps de développement d'une fonctionnalité qui dépend des équipes, de leur répartition des tâches et des compétences des individus au sein de ces équipes. Il y a également les choix d'architecture qui dépendent des objectifs et de l'ampleur du projet.

Pour les contraintes externes on peut noter la difficulté à recruter des personnes qualifiées, les deadlines liées aux clients et à leurs contraintes, ou encore les changements d'avis des clients qui peuvent avoir un fort impact avec l'utilisation des méthodes agiles.

### Les méthodes d'arbitrage

Il y a troix axes principaux en ce qui concerne les méthodes d'arbitrage, les statistiques, les recherches et l'expérimentation.

Les statistiques passent généralement par le monitoring ou les indicateurs clés de performance appelés KPI, la recherche utilise plutôt les études ou l'expérience des individus et l'expérimentation se base sur les tests internes ou externes en prenant en compte l'expérience des individus.

### Conclusion

Il existe différents types de prise de décision avec des méthodes qui leurs sont propres ou qui peuvent être transversales. Les décisions ont des impacts importants sur les équipes ainsi que sur l'entreprise et elles sont fortement influencées par les contraintes.

<div style="clear:both;page-break-after:always;"></div>

## 2. Gestion de la dette technique

### Qu’est-ce que la dette technique ?

La dette technique est le nom donné aux défauts du code qui compliquent l'ajout d'une fonctionnalité ou la maintenance. Elle doit être remboursée ce qui implique des coûts, du temps et des bugs.

#### Sources de la dette

Une conception logicielle négligée, le manque de temps, de connaîssance ou une mauvaise priorisation des tâches sont des sources importantes de dette. L'utilisation d'éléments externes comme des API ou des librairies qui évoluent en parallèle et impliquent aussi l'obsolescence de certaines parties du code.

### Pourquoi s'en soucier

La dette technique a des impacts à plusieurs échelles et peut avoir de graves conséquences, c'est pourquoi il est important de la réduire au maximum.

#### Impacts sur les développeurs

Du point de vue du code la dette implique des difficultés de lecture. Il est alors plus difficile de développer des fonctionnalités, plus facile d'introduire ou de corriger des bugs et cela a un impact sur le moral des développeurs. Il devient plus difficile de se motiver à travailler et changer de poste peut devenir attraillant.

#### Impacts sur les équipes

La dette pousse à augmenter les écarts entre les membres des équipes ce qui rend plus difficile l'attribution des tâches car seuls certaines personnes connaissent les spécificités du code liées à certaines parties de la dette. Des tensions peuvent apparaître entre certains membres et globalement le moral a tendence à baisser, et avec lui la productivité. Dans certains cas la réorganisation des équipes peut être envisagée pour limiter les effets de la dette.

#### Impacts sur l'entreprise

Dans le cas des projets internes, la dette implique un ralentissement du développement des applications et la présence de plus de bugs qui se traduit par une perte de croissance et une perte d'argent. L'élaboration des plannings de développement et la réalisation des devis deviennent aussi plus difficile. Pour les projets externes les coûts augmentent pour les clients et les relations peuvent se dégrader.

### Remboursement de la dette

Le remboursement de la dette passe par du refactoring voire par la réécriture de toute l'application. Il faut se baser sur ces expériences précédentes, passer du temps lors de la conception et ne pas choisir la facilité si elle n'est pas bénéfique au long terme.

### Conclusion

La dette technique est néfaste à différentes échelles et il est important de tout faire pour la réduire au maximum via des méthodes de conception et du remboursement.

<div style="clear:both;page-break-after:always;"></div>

## 3. Qualité, adéquation du produit avec la demande

En informatique, la qualité logicielle est une appréciation qui se base sur des indicateurs permettants de mesurer des éléments comme la performance, la fiabilité ou la tolérence aux pannes. Les deux principaux facteurs qui influent sur la qualité sont les coût et les délais.

### Analyse du besoin

Il est important de savoir à qui s'adresse un logiciel pour comprendre les besoins et définir les critères de qualité. Les besoins sont exprimés par les clients ou les utilisateurs finaux. On peut les retrouvé dans le cahier des charges et ils obéissent à des normes comme l'accessibilité, la sécurité ou la confidentialité.

### Adéquation du produit

Afin de valider le produit, le client doit fourni un cahier des charges qui détaille ses attentes.

### Qualité fonctionnelle

La qualité fonctionnelle a pour but de répondre aux besoins du client. Afin de réaliser un produit conforme, on sépare le produit en fonctionnalités afin de les traiter séparément. L'utilisation de diagrammes comme UML est préconisée afin d'exprimer un besoin technique tout en étant compréhensible par le client.

La méthode de gestion dépend du client. S'il est présent et réactif, les méthodes agiles peuvent maximiser le ciblage de ces besoins. S'il est peu présent, une méthode comme le cycle en V sera plus adaptée. Mettre en place un système de tickets est aussi un moyen efficace afin de suivre l'évolution des fonctionnalités, faire remonter des sisfonctionnements, définir les priorités et gérer les échéances.

L'utilisation d'environnements différents de la production, ainsi que la mise en place d'intégration continue et de tests automatisés permet d'assurer plusieurs critères de qualité en amont comme la fiabilité, la tolérence aux pannes et l'idempotence des systèmes.

### Qualité technique

Un code de faible qualité possède une forte dette technique. Elle rend difficile l'ajout de nouvelles fonctionnalités et facilite l'ajout de bugs, c'est pourquoi il est important d'en créer le moins possible.

Dans un premier temps les outils de versionning comme GIT, la réutilisabilité des composants, les commentaires dans le code ou encore les revues de code sont des moyens efficaces pour luter contre cette dette. Ensuite de nombreux problèmes en informatiques sont connus et peuvent être résolus efficacement par les design patterns. Enfin il est possible d'utiliser des outils d'analyse de code qui couplés avec les tests unitaires qui permettent de mesurer la couverture en tests du projet. Ce type d'outil peut être utilisé pour empêcher des mises en production si l'application ne respecte pas suffisament les critères de qualité.

### Conclusion

Afin de garantir la qualité d'un produit il faut comprendre les besoins du client et définir les indicateurs à utiliser. La qualité du code ne doit pas être négligée et de nombreux outils permettent de l'améliorer. Enfin la mise en place de tests est incontournable afin d'assurer la conformité avec les indicateurs définis.

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
