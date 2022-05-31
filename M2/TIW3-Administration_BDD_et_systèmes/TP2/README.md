# TIW3 - TP2

## Prérequis

Connexion à la VM puis à psql :

```shell=
$ ssh -i tiw3-asb-postgres.pem ubuntu@192.168.73.227
$ sudo -u postgres psql
```

Création de la base de données `benchdb` : 

```sql=
postgres=# create database benchdb;
postgres=# \c benchdb; 
/*
You are now connected to database "benchdb" as user "postgres".
*/
benchdb=# \q
```

Remplissage des données avec `pgbench`

```shell=
$ sudo -u postgres pgbench -i -s 10 benchdb
$ sudo -u postgres psql benchdb
```
```sql=
benchdb=# \dt;
              List of relations
 Schema |       Name       | Type  |  Owner   
--------+------------------+-------+----------
 public | pgbench_accounts | table | postgres
 public | pgbench_branches | table | postgres
 public | pgbench_history  | table | postgres
 public | pgbench_tellers  | table | postgres
(4 rows)

benchdb=# select count(*) from pgbench_tellers ;
 count 
-------
   100
(1 row)

benchdb=# select count(*) from pgbench_accounts;
  count  
---------
 1000000
(1 row)
```
## Étape 1

### Qu’est-ce qu’une sauvegarde full ?

Il s'agit d'une copie brute de toute la base de données.

### Effectuez une sauvegarde full.

```shell
# Create a backup file
pg_dumpall > pg_backup.bak
```

## Étape 2

### Supprimez la totalité des lignes de la table pgbench_tellers.

## Étape 3

### Qu’est-ce qu’une sauvegarde incrémentale ?

Cette sauvegarde conciste à mémoriser les modifications qui ont eu lieu en base depuis la dernière backup incrémentale.

### Quelle est la différence entre une sauvegarde incrémentale et une sauvegarde différentielle ?

La backup différentielle fonctionne exactement comme une backup incrémentale, sauf qu'elle se base sur la dernière full backup alors que la backup incrémentale se base sur elle même.

### Effectuez une sauvegarde incrémentale.

### Quelle est la différence entre une sauvegarde physique et une sauvegarde logique ?

Une sauvegarde physique est une compilation des fichiers qui composent la base de données, simple et rapide à restaurer mais dificilement lisible si on ouvre les fichiers. Une sauvegarde logique contient l'ensemble des données dans un format texte facilement lisible, mais est plus lente à restaurer.

## Que signifie WAL ?

**Write-Ahead Logging**, il s'agit des journaux de transactions de la base de données qui permettent d'assurer la cohérence des données dans le processus de restauration en cas d'arrêt imprévu de la base.

## Pourquoi a-t-on besoin des WALs lors d’une sauvegarde physique ?

> What's more, the physical backup doesn't have to be an instantaneous snapshot of the database state — if it is made over some period of time, then replaying the WAL log for that period will fix any internal inconsistencies.

*[postgresql.org](https://www.postgresql.org/docs/current/wal-intro.html)*

La copie des fichiers de la base de données peuvent être modifiés lors de la sauvegarde, étant donné que ce n'est pas un processus instantanné. Les WALs sont alors nécessaires pour rétablir la cohérence.

## Étape 4

### Que signifie PITR ?

> PITR est l'acronyme de **Point In Time Recovery**, autrement dit restauration à un point dans le temps.
> [...] C’est une sauvegarde à chaud et surtout en continu. Là où une sauvegarde logique du type pg_dump se fait au mieux une fois toutes les 24 h, la sauvegarde PITR se fait en continu grâce à l’archivage des journaux de transactions. De ce fait, ce type de sauvegarde diminue très fortement la fenêtre de perte de données.

[*public.dalibo.com*](https://public.dalibo.com/exports/formation/manuels/modules/i2/i2.handout.html)

### Supprimez les lignes de pgbench_accounts pour lesquelles la colonne bid vaut 2.

## Étape 5

### Vérifiez le nombre de lignes dans la table pgbench_accounts.

## Étape 6

### Restaurez la base dans l’état dans lequel elle était avant l’étape 4.

## Étape 7

### Vérifiez le nombre de lignes dans la table pgbench_accounts.

## Étape 8

### Restaurez la base dans l’état dans lequel elle était avant l’étape 2.

## Étape 9

### Vérifiez le nombre de lignes dans les tables pgbench_tellers et pgbench_accounts.

