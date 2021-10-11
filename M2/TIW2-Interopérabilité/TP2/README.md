# TP noté netoyage de données

Julien Giraud p1704709

Ce TP a été réalisé sur une base postgres.

## Notes

### Remplissage de la bd

```shell
psql -h localhost -U user -d tiw2 < script.sql
```

### N. Format de l'erreur N

#### N.1 Explication du problème

Le problème … :

- il s'agit d'une erreur de type *violations de dépendances fonctionnelles | violations de dépendances fonctionnelles conditionnelles | problèmes de doublons | problèmes de données manquantes*,
- on peut la détecter avec …,
- on peut la corriger en … .

#### N.2 Requête(s) SQL pour détecter

 ```sql
  SELECT * FROM projet WHERE "SIREN" NOT SIMILAR TO '(0|1|2|3|4|5|6|7|8|9){9}';
  ```

#### N.3 Requête(s) SQL pour corriger

  ```sql
  ALTER TABLE projet SET "SIREN" = NULL WHERE "SIREN" NOT SIMILAR TO '(0|1|2|3|4|5|6|7|8|9){9}';
  ```

## Erreurs

### 1. La valeur du code siret

#### 1.1 Explication du problème

Le code siret doit être composé de 9 chiffres :

- il s'agit d'une erreur de type *Violations de dépendances fonctionnelles*,
- on peut la détecter avec un regex, par exemple `^[0-9]{9}$`,
- on peut la corriger en passant les valeurs invalides à `NULL`.

#### 1.2 Requête(s) SQL pour détecter

 ```sql
  SELECT * FROM projet WHERE "SIREN" NOT SIMILAR TO '(0|1|2|3|4|5|6|7|8|9){9}';
  ```

#### 1.3 Requête(s) SQL pour corriger

  ```sql
  ALTER TABLE projet SET "SIREN" = NULL WHERE "SIREN" NOT SIMILAR TO '(0|1|2|3|4|5|6|7|8|9){9}';
  ```
