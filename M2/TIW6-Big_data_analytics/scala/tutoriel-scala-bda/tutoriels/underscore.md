# Notation '_'

Le caractère `_` peut être utilisé de [nombreuses manières](https://stackoverflow.com/questions/8000903/what-are-all-the-uses-of-an-underscore-in-scala) en Scala

Dans un interpréteur, évaluer les expressions suivantes correspondant à différentes utilisations de `_`.

## Paramètre anonyme

Remplace le nom d'un paramètre inutilisé dans une fonction

```scala
val f = (_:String) => 3
```

## Ignorer une valeur dans un pattern matching

```scala
case class Toto(x: Int, y: Int)

new Toto(3,5) match  {
case Toto(_,a) => println(a)
}
```
## Import d'un package complet

```scala
import java.util._
```
est équivalent à
```java
import java.util.*;
```

## Abbréviation dans la définition d'une fonction

```scala
val appPlus = (f: Int => Int, x: Int) => (f(x)+3)
val y = appPlus({_*2},5) 
```
est équivalent à:
```scala
val appPlus = (f: Int => Int, x: Int) => (f(x)+3)
val y = appPlus(((x)=>x*2), 5) 
```
