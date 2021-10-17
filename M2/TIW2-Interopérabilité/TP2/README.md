# TIW2 : TP noté sur le Data Cleaning, nettoyage de données avec SQL

- Jeremy Thomas p1702137
- Julien Giraud p1704709

Ce TP a été réalisé sur une base PostgreSQL. Les correctifs ne sont pas forcément listés dans l'ordre optimum pour nettoyer les données.

## Notes

### Remplissage de la table

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

### 1. Le code SIREN

#### 1.1 Explication du problème

Le code SIREN est un code Insee unique qui sert à identifier une entreprise et doit être composé de 9 chiffres et différent de `000000000`. Son absence est parfois signifiée par `Inconnu`, `Indétermi` ou `N/C`  :

- il s'agit d'une erreur de type *Problème de donnée manquante* car le SIREN permet d'identifier une entreprise,
- on peut la détecter avec une regex, par exemple `[0-9]{9}` et non `0{9}`,
- on peut la corriger en passant les valeurs invalides à `null`.

**Note** : ici nous ne traitons que la syntaxe du code SIREN, pour plus de rigueur nous devrions vérifier le chiffre de contrôle comme indiqué sur [ce site](https://portal.hardis-group.com/pages/viewpage.action?pageId=120357227). Cette vérification est particulièrement difficile à implémenter en SQL, c'est pourquoi nous nous sommes contenté de la syntaxe.

#### 1.2 Requête SQL pour détecter

```sql
select * from projet WHERE "SIREN" not similar to '[0-9]{9}' or "SIREN" = '000000000';
```

#### 1.3 Requête SQL pour corriger

```sql
-- Passage à null des SIREN non valides 
update projet set "SIREN" = null where "SIREN" not similar to '[0-9]{9}' or "SIREN" = '000000000';
-- Changement du type de la colonne en numeric
alter table projet alter column "SIREN" type numeric(9,0) USING "SIREN"::numeric(9,0);
```

<div style="page-break-after:always"></div>

### 2. Le code NIC

#### 2.1 Explication du problème

Le code NIC permet d’identifier l’établissement au sein de l’unité légale (SIREN) à laquelle il est rattaché et doit être est composé de 5 chiffres et différent de `00000` :

- il s'agit d'une erreur de type *Problème de donnée manquante* car lorsque le SIREN est connu, le NIC permet d'identifier un établissement,
- on peut la détecter avec une regex appliqué sur les lignes dont le code SIREN est valide, par exemple `[0-9]{5}` et non `0{5}`,
- on peut la corriger en passant les valeurs invalides à `null`.

#### 2.2 Requête(s) SQL pour détecter

```sql
select * from projet where "SIREN" is not null and ("NIC" not similar to '[0-9]{5}' or "NIC" = '00000');
```

#### 2.3 Requête(s) SQL pour corriger

```sql
-- Passage à null des NIC non valides 
update projet set "NIC" = null where "NIC" not similar to '[0-9]{5}' or "NIC" = '00000';
```

### 3. Remplissage du code NIC

#### 3.1 Explication du problème

Le code NIC doit être associé au code SIREN afin de former le code SIRET = (SIREN + NIC) qui identifie (entre autre) une structure et son adresse :

- il s'agit d'une erreur de type *Problèmes de données manquantes*,
- on peut la détecter en filtrant les lignes avec un code SIREN mais pas de code NIC,
- on peut éventuellement requêter l'API Sirene de l'INSEE afin de récupérer les codes NIC associés au code SIREN mais il faut trouver un moyen fiable de choisir le bon code NIC. Si le problème persiste et que le code NIC devient nécessaire il est possible de supprimer les lignes en question.

#### 3.2 Requête(s) SQL pour détecter

```sql
select * from projet where "SIREN" is not null and "NIC" is null;
```

<div style="page-break-after:always"></div>

#### 3.3 Requête(s) SQL pour corriger

```sql
-- Si le code SIRET = SIREN + NIC est absolument nécessaire, on ne peut pas se permettre d'avoir des NIC null, donc on les supprime
delete from projet where "SIREN" is not null and "NIC" is null;
```

### 4. Situation SIRENE incohérente

#### 4.1 Explication du problème

Le champ *Situation SIRENE* permet de commenter les éléments du code SIRET = (SIREN + NIC). Il doit donc être vide lorsque le SIRET  et le NIC sont valides, ce qui n'est pas toujours le cas :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles conditionnelles*,
- on peut la détecter en filtrant les lignes qui renseigne cet élément et qui ont un SIREN et un NIC valide,
- on peut la corriger en passant à `null` les champs qui devraient être vide.

#### 4.2 Requête(s) SQL pour détecter

```sql
select "Situation SIRENE", "SIREN", "NIC" from projet where "Situation SIRENE" <> '' and "SIREN" is not null and "NIC" is not null;
```

#### 4.3 Requête(s) SQL pour corriger

```sql
-- Passage à null de Situation Sirene s'il ne l'est pas alors que l'on connait le SIREN et le NIC (oublie de mise à jour du champs après avoir entré le SIREN ou le NIC par exemple)
update projet set "Situation SIRENE" = null where "Situation SIRENE" <> '' and "SIREN" is not null and "NIC" is not null;
```

### 5. Identification des communes

#### 5.1 Explication du problème

La localisation d'une organisation est identifiée par le triplet `code département`, `code commune`, `ville ou pays` qui est dupliqué sur plusieurs lignes :

- il s'agit d'une erreur de type *Problèmes de doublons*,
- on peut la détecter en comptant le nombre de triplets dont l'occurrence est supérieure à 1,
- on peut la corriger en déplaçant les triplets dans une table *commune* et en liant les lignes à la table *commune* avec une clé étrangère.

#### 5.2 Requête(s) SQL pour détecter

```sql
select "COG : code département" , "COG : code commune", "COG : ville ou pays", count(*)
from projet group by "COG : code département" , "COG : code commune", "COG : ville ou pays"
having count(*) > 1;
```

#### 5.3 Requête(s) SQL pour corriger

```sql
-- Création de la table lieu, qui accueillera les données sur la localisation de l'organisation
drop table if exists lieu;
create table lieu (
    id bigserial primary key,
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
-- Suppression des colonnes désormais inutiles
alter table projet
    drop column "COG : code département",
    drop column "COG : code commune",
    drop column "COG : ville ou pays";
```

<div style="page-break-after:always"></div>

### 6. Format de la réserve 2016

#### 6.1 Explication du problème

La colonne `Réserve 2016` représente un champs booléen dont la valeur true peut prendre la valeur `x`, `oui`, `OUI` ou encore `Oui` :

- il s'agit d'une erreur de type *Problème de donnée manquante (pas de cohérence dans le remplissage)*,
- on peut la détecter regardant si le champs est null car la valeur false est représenté par un champs vide,
- on peut la corriger en convertissant la colonne en booléen en remplaçant les champs non null par true et les champs `null` par `false`.

#### 6.2 Requête(s) SQL pour détecter

```sql
select * from projet where "Réserve 2016" <> ''
```

#### 6.3 Requête(s) SQL pour corriger

```sql
-- Passage à true des champs Réserve 2016 s'ils sont non vide, à false sinon.
update projet
set "Réserve 2016" =
    case when "Réserve 2016" <> '' then true else false
end;
-- Changement du type de la colonne à booléen
alter table projet alter column "Réserve 2016" type boolean using "Réserve 2016"::boolean;
```

### 7. Format du code RNA

#### 7.1 Explication du problème

D'après le site du gouvernement, le numéro RNA permet l'identification des associations et est composé de la lettre `W` suivi de 9 chiffres. À noter que certains numéros possèdent une lettre parmi les 9 chiffres, par exemple l'association pour les déficients sensoriels de Mayotte. dont le numéro RNA est W9T1000765.

- il s'agit d'une erreur de type *Problème de donnée manquante*,
- on peut la détecter à l'aide de regex récupérant les numéro RNA qui ne correspondent pas au bon format,
- on peut la corriger en passant les valeurs invalides à `null` ou en ajoutant la lettre `W` pour les numéros possédant les 9 chiffres.

<div style="page-break-after:always"></div>

#### 7.2 Requête(s) SQL pour détecter

```sql
select * from projet where "RNA" <> '' and "RNA" not similar to 'W[0-9A-Z]{9}'
```

#### 7.3 Requête(s) SQL pour corriger

```sql
-- Si le RNA est vide, le champs devient null
-- Si le RNA contient un W et 8 chiffres, il est incomplet et devient null
-- Si le RNA contient 9 chiffre, il ne manque que le W, on l'ajoute alors
update projet 
set "RNA" =
    case when "RNA" = '' then null
    when "RNA" <> '' and "RNA" like 'W%' and "RNA" similar to '[0-9A-Z]{9}' then null
    when "RNA" <> '' and "RNA" not like 'W%' and "RNA" similar to '[0-9A-Z]{9}' then CONCAT('W', "RNA")
end;
```

### 8. Numérotation des département

#### 8.1 Explication du problème

Les départements français sont numérotés de 1 à 95. Le numéro des départements d'outre-mer commencent par 97 et sont suivis d'un chiffre. Or, dans les données, seul 97 est répertorié dans le code_departement.

- il s'agit d'une erreur de type *Violation de dépendance fonctionnelle conditionnelle*,
- on peut la détecter à l'aide de regex récupérant les de numéro 97,
- on peut la corriger en récupérant le troisième chiffre du département puisqu'il s'agit du premier chiffre du code de la commune.

#### 8.2 Requête(s) SQL pour détecter

```sql
-- Nécessite d'avoir créé la table lieu à la 4.3
select * from lieu where code_departement = '97';
```

<div style="page-break-after:always"></div>

#### 8.3 Requête(s) SQL pour corriger

```sql
-- Nécessite d'avoir appliqué le correctif 4.3
alter table lieu alter column "code_departement" type varchar(3);
-- Récupération du premier chiffre de la commune afin d'obtenir le département (Exemple : 97 + 4xx = 974, La Réunion)
update lieu 
set "code_departement" = concat("code_departement", left("code_commune",1))
where "code_departement" = '97';
```

### 9. Identification des organisations

#### 9.1 Explication du problème

Les établissements concernent les colonnes `SIREN`, `NIC`, `Dénomination`, `Nomenclature juridique`, `Code NAF`, `Situation SIRENE` et `RNA` et sont dupliquées sur plusieurs lignes :

- il s’agit d’une erreur de type *Problème de doublons*,
- on peut la détecter en comptant le nombre de tuples dont l’occurrence est supérieure à 1,
- on peut la corriger en déplaçant les tuples dans une table *etablissement* et en liant les lignes à la table avec une clé étrangère.

#### 9.2 Requête(s) SQL pour détecter

```sql
select "SIREN", "NIC", "Dénomination", "Nomenclature juridique", "Situation SIRENE", "Code NAF", "RNA", count(*) 
from projet
group by "SIREN", "NIC", "Dénomination", "Nomenclature juridique", "Code NAF","Situation SIRENE", "RNA" 
having count(*) > 1
```

<div style="page-break-after:always"></div>

#### 9.3 Requête(s) SQL pour corriger

```sql
-- Création de la table qui accueillera les données sur les organisations
drop table if exists etablissement;
create table etablissement(
    id BIGSERIAL primary key,
    siren numeric(9),
    nic varchar(5),
    nom varchar(200),
    nomenclature_juridique numeric(4),
    naf varchar(5),
    rna varchar(10),
    situation_siren varchar(300)
);
-- Remplissage de la table
-- Updated Rows: 40127
insert into etablissement(siren, nic, nom, nomenclature_juridique, naf, rna, situation_siren)
    select distinct "SIREN", "NIC", upper("Dénomination"), cast("Nomenclature juridique" as numeric), "Code NAF", "RNA", upper("Situation SIRENE")
    from projet;
-- Ajout de la clé étrangère "organisation" dans projet
alter table projet add column etablissement_id integer;
alter table projet add constraint fk_etablissement foreign key (etablissement_id) references etablissement(id);

-- ATTENTION : Appliquer le correctif 10 avant d'effectuer cette mise à jour

-- Remplissage de l'organisation dans projet
-- Updated Rows: 56167
update projet set etablissement_id = (
    select id from etablissement
    where siren = "SIREN" and nic = "NIC" 
) where "SIREN" is not null;
-- Suppression des colonnes désormais inutiles
alter table projet
    drop column "SIREN",
    drop column "NIC",
    drop column "Dénomination",
    drop column "Nomenclature juridique",
    drop column "Code NAF",
    drop column "RNA",
    drop column "Situation SIRENE";
```

<div style="page-break-after:always"></div>

### 10. Identification d'un établissement

#### 10.1 Explication du problème

Un établissement est identifiable par son `SIREN` et son `NIC`. Il ne devrait donc y avoir qu'un seul établissement pour un couple `SIREN` et `NAF` donné. Or, dans les données, certains établissements apparaissent en doublons car leur `NAF` est différent (alors qu'en cas de pluriactivité, l’entreprise recevra malgré tout un seul et unique code `NAF`, correspondant à son activité principale) ou que leur dénomination sociale comporte des coquilles (faute de frappe, minuscule/majuscule, tirets…) :

- il s’agit d’une erreur de type *Problème de doublons*,
- on peut la détecter en comptant le nombre de couple `SIREN` et `NAF`dont l’occurrence est supérieure à 1,
- on peut la corriger en ne gardant que la ligne correspond au premier couple trouvé, en espérant qu'il s'agisse du bon code NAF et du nom de l'établissement le mieux écrit.

#### 10.2 Requête(s) SQL pour détecter

```sql
-- Nécessite d'avoir appliqué le correctif 9.3
-- Récupère les lignes en doublons qui ont le meme couple siren et nic mais un nom different (coquille)
select siren, nic, string_agg(nom, '----') from etablissement where siren is not null group by siren, nic having count(*) > 1;
```

#### 10.3 Requête(s) SQL pour corriger

```sql
-- Suppression des doublons 
-- Updated rows 287
delete from etablissement 
where id in (
    select e1.id from etablissement e1, etablissement e2 
    where e1.id < e2.id and e1.siren = e2.siren and e1.nic = e2.nic
);

-- Après avoir supprimé les établissements en doublon, des etablissement_id dans projet peuvent avoir été supprimé. Il est alors nécessaire soit d'appliquer le correctif 10 avant d'importer les id dans le 9.3 soit de mettre à nouveau à jour les id
update projet set etablissement_id = (
    select id from etablissement
    where 
        siren = "SIREN" and
        nic = "NIC"
) where "SIREN" is not null;
```
