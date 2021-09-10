# Tutoriel Scala pour l'UE BigData Analytics

## Environnement de travail

> Attention: si vous utilisez les machines de TP, configurer votre compte comme indiqué [dans l'aide](http://liris.cnrs.fr/~ecoquery/dokuwiki/doku.php?id=enseignement:aide:maven) (faires les deux configurations: maven et sbt)

[FAQ de la forge](https://forge.univ-lyon1.fr/EMMANUEL.COQUERY/forge/wikis/FAQ)

Créer un projet sur https://forge.univ-lyon1.fr

Cloner le projet

Depuis le répertoire local, récupérer l'énoncé:

```
git pull https://forge.univ-lyon1.fr/EMMANUEL.COQUERY/tutoriel-scala-bda.git
```

Installer les logiciels suivants

- Java 1.11+, par exemple version [AdoptOpenJDK](https://adoptopenjdk.net/)
- [SBT](https://www.scala-sbt.org/download.html)
- Si vous utilisez:
  - IntelliJ/Idea, installer le plugin Scala
  - Eclipse, installer le plugin [Scala-IDE](http://scala-ide.org/) pour Eclipse
  - VS-Code, installer le plugin [Metals](https://marketplace.visualstudio.com/items?itemName=scalameta.metals)
- Configurer au besoin le proxy HTTP de Lyon 1
  ```
  export http_proxy=http://proxy.univ-lyon1.fr:3128
  ```

Remarque: scala et sbt devraient être sous Linux en salle TP.

Si vous n'arrivez pas à installer Scala en ligne de commande (i.e. l'interpréteur `scala` n'est pas disponible), il est possible d'utiliser https://scalafiddle.io/ à la place. Il est également possible, dans un projet géré par `sbt`, d'utiliser la commande `sbt console`.

## Hello World

Suivre le tutoriel [Scala+SBD](http://www.scala-lang.org/documentation/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html)

## Valeurs, types et classes

Suivres les tutoriels suivants: [Basics](http://docs.scala-lang.org/tour/basics.html), [Types de base](http://docs.scala-lang.org/tour/unified-types.html), [Classes](http://docs.scala-lang.org/tour/classes.html)

## Tester

Suivre le tutoriel sur [ScalaTest avec sbt](http://www.scala-lang.org/documentation/getting-started-sbt-track/testing-scala-with-sbt-on-the-command-line.html)
Si la mise en place de l'exemple pose problème, utiliser à la place le mini projet `scala-test-example`

## Case classes, structures fréquement utilisées

Suivre le tutoriel sur les [Case classes](http://docs.scala-lang.org/tour/case-classes.html) et le [Pattern Matching](http://docs.scala-lang.org/tour/pattern-matching.html)

Faire les exercices sur les [Options](https://www.scala-exercises.org/std_lib/options), les [Tuples](https://www.scala-exercises.org/std_lib/tuples), les [Lists](https://www.scala-exercises.org/std_lib/lists) et les [Maps](https://www.scala-exercises.org/std_lib/maps).

## Ordre supérieur

Suivre le tutoriel sur les [fonctions d'ordre supérieur](http://docs.scala-lang.org/tour/higher-order-functions.html) et sur la notation [underscore \_](tutoriels/underscore.md), puis faire les [exercices](https://www.scala-exercises.org/std_lib/higher_order_functions).

Faire les exercices sur [les opérateurs](https://www.scala-exercises.org/std_lib/infix_prefix_and_postfix_operators).

## Trait

Suivre le tutoriel sur les [Traits](http://docs.scala-lang.org/tour/traits.html) et les [Mixins](http://docs.scala-lang.org/tour/mixin-class-composition.html).

## Traitements en flux

Faire les exercices sur les [Traversables](https://www.scala-exercises.org/std_lib/traversables).

Suivre le tutoriel sur les compréhensions [for](http://docs.scala-lang.org/tour/for-comprehensions.html) et [séquences](http://docs.scala-lang.org/tour/sequence-comprehensions.html).
Faire les exercices sur les [for expressions](https://www.scala-exercises.org/std_lib/for_expressions)

## Entrées / Sorties

Lire le [tutoriel sur les entrées/sorties](https://www.tutorialspoint.com/scala/scala_file_io.htm).

## Exercice

Faire [l'exercice sur la gestion de fichiers CSV & JSON](tutoriels/exercice_csv.md)

## Ressources

- http://www.scala-lang.org/documentation/getting-started.html
- http://www.scala-lang.org/documentation/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html
- https://www.scala-exercises.org/
