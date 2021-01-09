# TP MongoDB

## Questions

### EX1 Q2

Trouvez la commande MongoDB pour afficher un document de la collection zips. Expliquer la structure du document trouvé.

```mongo
> db.zips.find({});
{ "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA" }
{ "_id" : "01002", "city" : "CUSHMAN", "loc" : [ -72.51565, 42.377017 ], "pop" : 36963, "state" : "MA" }
...
```

### EX1 Q3

Trouvez la commande MongoDB pour calculer le nombre de documents de la collection zips.

```mongo
> db.zips.find({}).length();
29353
```

### EX1 Q4

Reprendre les questions précédentes avec les collections grades et restaurants.

#### Grades

```mongo
> db.grades.find({});
{ "_id" : ObjectId("50b59cd75bed76f46522c35f"), "student_id" : 2, "class_id" : 27, "scores" : [ { "type" : "exam", "score" : 70.32953992025745 }, { "type" : "quiz", "score" : 66.24220071248318 }, { "type" : "homework", "score" : 79.21965885764142 }, { "type" : "homework", "score" : 78.68052791237751 } ] }
{ "_id" : ObjectId("50b59cd75bed76f46522c360"), "student_id" : 2, "class_id" : 24, "scores" : [ { "type" : "exam", "score" : 76.01876674517686 }, { "type" : "quiz", "score" : 47.44729578274631 }, { "type" : "homework", "score" : 4.735101893467009 }, { "type" : "homework", "score" : 92.65331076863312 } ] }
...
> db.grades.find({}).length();
280
```

#### Restaurants

```mongo
> db.restaurants.find({});
{ "_id" : ObjectId("55cba2476c522cafdb053add"), "location" : { "coordinates" : [ -73.856077, 40.848447 ], "type" : "Point" }, "name" : "Morris Park Bake Shop" }
{ "_id" : ObjectId("55cba2476c522cafdb053ade"), "location" : { "coordinates" : [ -73.961704, 40.662942 ], "type" : "Point" }, "name" : "Wendy'S" }
...
> db.restaurants.find({}).length();
25359
```

### EX1 Q5

Trouvez la commande MongoDB qui permet de donner la liste des zips de l’état de Californie.

```mongo
> db.zips.find({"state" : "CA"});
```

### EX1 Q6

Même question que précédemment, mais cette fois vous ne voulez garder dans le résultat que le nom de la ville et aucun autre champ.

```mongo
> db.zips.find({"state" : "CA"}, {"city": ""});
```

### EX1 Q7

Trouvez la commande MongoDB qui permet de lister les zips dont la population est supérieure à 100.000 habitants. Même question avec le nombre de zips dont la population est supérieure à 100.000 habitants.

```mongo
> db.zips.find({"pop" : {$gt: 100000}});
{ "_id" : "10021", "city" : "NEW YORK", "loc" : [ -73.958805, 40.768476 ], "pop" : 106564, "state" : "NY" }
{ "_id" : "10025", "city" : "NEW YORK", "loc" : [ -73.968312, 40.797466 ], "pop" : 100027, "state" : "NY" }
{ "_id" : "11226", "city" : "BROOKLYN", "loc" : [ -73.956985, 40.646694 ], "pop" : 111396, "state" : "NY" }
{ "_id" : "60623", "city" : "CHICAGO", "loc" : [ -87.7157, 41.849015 ], "pop" : 112047, "state" : "IL" }
> db.zips.find({"pop" : {$gt: 100000}}).length();
4
```
