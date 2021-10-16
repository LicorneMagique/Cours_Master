# TP noté netoyage de données

Julien Giraud p1704709

Ce TP a été réalisé sur une base postgres.

## notes

### Remplissage de la bd

```shell
psql -h localhost -U user -d tiw2 < script.sql
```

### N. Format de l'erreur N

#### N.1 Explication du problème

Le problème … :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles | Violations de dépendances fonctionnelles conditionnelles | Problèmes de doublons | Problèmes de données manquantes*,
- on peut la détecter avec …,
- on peut la corriger en … .

#### N.2 Requête(s) SQL pour détecter

```sql
```

#### N.3 Requête(s) SQL pour corriger

```sql
```

## Erreurs

### 1. Le format du code SIREN

#### 1.1 Explication du problème

Le code SIREN doit être composé de 9 chiffres :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles*,
- on peut la détecter avec un regex, par exemple `^[0-9]{9}$`,
- on peut la corriger en passant les valeurs invalides à `null`.

#### 1.2 Requête(s) SQL pour détecter

```sql
select * from projet WHERE "SIREN" not similar to '(0|1|2|3|4|5|6|7|8|9){9}';
```

#### 1.3 Requête(s) SQL pour corriger

```sql
update projet set "SIREN" = null where "SIREN" not similar to '(0|1|2|3|4|5|6|7|8|9){9}';
```

### 2. Le format du code NIC

#### 2.1 Explication du problème

Le code NIC doit être est composé de 5 chiffres :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles conditionnelles*,
- on peut la détecter avec un regex appliqué sur les lignes dont le code SIREN est valide, par exemple `^[0-9]{5}$`,
- on peut la corriger en passant les valeurs invalides à `null` .

#### 2.2 Requête(s) SQL pour détecter

```sql
-- Cette requête suppose que le correctif 1.3 a été utilisé,
-- autrement dit tous les codes SIREN non null sont valides.
select * from projet where "SIREN" IS not null AND "NIC" not similar to '(0|1|2|3|4|5|6|7|8|9){5}';
```

#### 2.3 Requête(s) SQL pour corriger

```sql
-- Mêmes prérequis que la 2.2.
select * from projet where "SIREN" IS not null AND "NIC" not similar to '(0|1|2|3|4|5|6|7|8|9){5}';
```

### 3. Remplissage du code NIC

#### 3.1 Explication du problème

Le code NIC doit être associé au code SIREN afin de former le code SIRET (SIREN+NIC) qui identifie (entre autre) une structure et son adresse :

- il s'agit d'une erreur de type *Problèmes de données manquantes*,
- on peut la détecter en filtrant les lignes avec un code SIREN mais pas de code NIC,
- on peut éventuellement requêter l'API Sirene de l'INSEE afin de récupérer les codes NIC associés au code SIREN mais il faut trouver un moyen fiable de choisir le bon code NIC. Si le problème persiste et que le code NIC devient nécessaire il est possible de supprimer les lignes en question.

#### 3.2 Requête(s) SQL pour détecter

```sql
select * from projet where "SIREN" IS not null AND "NIC" IS null;
```

#### 3.3 Requête(s) SQL pour corriger

```sql
-- À n'utiliser que si le code SIRET est absolument nécessaire.
DELETE from projet where "SIREN" IS not null AND "NIC" IS null;
```

### 4. Situation SIRENE incohérente

#### 4.1 Explication du problème

Le champ *Situation SIRENE* permet de commenter les éléments du code siret (SIREN+NIC). Il doit donc être vide lorsque le SIRET est valide ce qui n'est pas toujours le cas :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles conditionnelles*,
- on peut la détecter en filtrant les lignes qui renseigne cet élément et qui ont un code SIRET valide,
- on peut la corriger en passant à `null` les champs qui devraient être vide.

#### 4.2 Requête(s) SQL pour détecter

```sql
-- Cette requête suppose que le correctif 3.3 a été utilisé,
-- autrement dit tous les codes SIREN ont un code NIC valide.
select * from projet where "Situation SIRENE" is not null and "NIC" is not null;
```

#### 4.3 Requête(s) SQL pour corriger

```sql
-- Mêmes prérequis que la 4.2.
update projet set "Situation SIRENE" = null where "Situation SIRENE" is not null and "NIC" is not null;
```

### 5 Identification des communes

#### 5.1 Explication du problème

Les communes sont identifiées par le triplet *code département, code commune, ville ou pays* qui est dupliqué sur plusieurs lignes :

- il s'agit d'une erreur de type *Problèmes de doublons*,
- on peut la détecter en comptant le nombre de triplets dont l'occurence est supérieure à 1,
- on peut la corriger en déplaçant les triplets dans une table *commune* et en liant les lignes à la table *commune* avec une clé étrangère.

#### 5.2 Requête(s) SQL pour détecter

```sql
select "COG : code département" , "COG : code commune", "COG : ville ou pays"
from projet GROUP BY "COG : code département" , "COG : code commune", "COG : ville ou pays"
HAVING COUNT(*) > 1;
```

#### 5.3 Requête(s) SQL pour corriger

```sql
-- Création de la table
drop table if exists lieu;
create table lieu (
    id BIGSERIAL primary key,
    code_departement varchar(2),
    code_commune varchar(3),
    ville_ou_pays varchar(50)
);
-- Remplissage de la table
-- Updated Rows: 7087
insert into lieu (code_departement, code_commune, ville_ou_pays)
    select distinct "COG : code département", "COG : code commune", "COG : ville ou pays"
from projet;
-- Ajout de la clé étrangère "lieu" dans projet
alter table projet add column lieu_id integer;
alter table projet add constraint fk_lieu foreign key (lieu_id) references lieu(id);
-- Remplissage du lieu dans projet
-- Updated Rows: 56487
update projet set lieu_id = (
    select id from lieu
    where
        code_departement = "COG : code département" and
        code_commune = "COG : code commune" and
        ville_ou_pays = "COG : ville ou pays"
);
-- Suppression des données dupliquées
alter table projet
    drop column "COG : code département",
    drop column "COG : code commune",
    drop column "COG : ville ou pays";
```
