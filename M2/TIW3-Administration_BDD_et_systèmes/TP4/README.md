# TP4 : SQL

## Binome

- Jeremy Thomas p1702137
- Julien Giraud p1704709

## Création de la base

Nous utilisons une base avec un docker-compose

```yml
# docker-compose.yml
version: "3.4"
volumes:
  data:
services:
  postgres:
    image: "postgres:14"
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_USER: postgres
      POSTGRES_DB: chinook
    volumes:
      - ./postgres-data:/var/lib/postgresql
```

## Import de données

```shell
wget https://l_avrot.gitlab.io/tiw-postgres/chinook.sql.gz && gunzip chinook.sql.gz
psql -U postgres chinook -h localhost < chinook.sql > /dev/null
# password
```

## Jointure latérale

```sql
select
    e1.last_name employee_last_name,
    e1.first_name employee_first_name,
    s.first_name superior_first_name,
    s.last_name superior_last_name
from
    employees e1,
    lateral (
        select
            e2.first_name,
            e2.last_name
        from employees e2
        where e1.reports_to = e2.id
    ) s;

```

```txt
employee_last_name|employee_first_name|superior_first_name|superior_last_name|
------------------+-------------------+-------------------+------------------+
Edwards           |Nancy              |Andrew             |Adams             |
Peacock           |Jane               |Nancy              |Edwards           |
Park              |Margaret           |Nancy              |Edwards           |
Johnson           |Steve              |Nancy              |Edwards           |
Mitchell          |Michael            |Andrew             |Adams             |
King              |Robert             |Michael            |Mitchell          |
Callahan          |Laura              |Michael            |Mitchell          |
```

## Aggrégations avancées

### Grouping sets

```sql
-- Nous allons dans un premier temps calculer le total de chaque facture (un
-- simple group by devrait suffire).
select
    invoice_id,
    sum(unit_price * quantity) total
from invoice_lines
group by invoice_id;
```

```txt
invoice_id|total|
----------+-----+
         1| 1.98|
         2| 3.96|
         3| 5.94|
         4| 8.91|
         5|13.86|
         6| 0.99|
         7| 1.98|
         8| 1.98|
         9| 3.96|
        10| 5.94|
...
```

```sql
-- Puis nous calculerons le total de toutes les factures pour chaque mois de 
-- l’année 2012 et la dernière ligne donnera le total pour toute l’année 2012
-- (la colonne mois pour cette ligne pourra être nulle).
select
    date_part('month', invoice_date) "month",
    sum(unit_price * quantity) total
from invoice_lines il
    join invoices i on i.id = il.invoice_id
where 
    invoice_date >= '2012-01-01 00:00:00'
    and invoice_date < '2013-01-01 00:00:00'
group by grouping sets (("month"), ())
order by "month";
```

```txt
month|total |
-----+------+
  1.0| 37.62|
  2.0| 37.62|
  3.0| 37.62|
  4.0| 37.62|
  5.0| 37.62|
  6.0| 37.62|
  7.0| 39.62|
  8.0| 47.62|
  9.0| 46.71|
 10.0| 42.62|
 11.0| 37.62|
 12.0| 37.62|
     |477.53|
```

### Window functions

```sql
-- Vous souhaitez récupérer en une seule requête pour chaque client son nom,
-- son prénom ainsi que le nombre total de clients.
select * from customers;
select first_name, last_name, count(id)
over ()
from customers;
```

```txt
first_name|last_name   |count|
----------+------------+-----+
Luís      |Gonçalves   |   59|
Leonie    |Köhler      |   59|
François  |Tremblay    |   59|
Bjørn     |Hansen      |   59|
František |Wichterlová |   59|
Helena    |Holý        |   59|
Astrid    |Gruber      |   59|
Daan      |Peeters     |   59|
Kara      |Nielsen     |   59|
Eduardo   |Martins     |   59|
...
```

## Recursive CTE

```sql
with recursive included_employees(id, first_name, last_name, reports_to) as (
    select
        e.id,
        e.first_name,
        e.last_name,
        e.reports_to 
    from employees e
    where e.first_name = 'Andrew' and e.last_name = 'Adams'
    
    union all
    
    select
        e.id,
        e.first_name,
        e.last_name,
        e.reports_to
    from included_employees ie
        join employees e on e.reports_to = ie.id
)
select *
from included_employees
where not (first_name = 'Andrew' and last_name = 'Adams');
```

```txt
id|first_name|last_name|reports_to|
--+----------+---------+----------+
 2|Nancy     |Edwards  |         1|
 6|Michael   |Mitchell |         1|
 3|Jane      |Peacock  |         2|
 4|Margaret  |Park     |         2|
 5|Steve     |Johnson  |         2|
 7|Robert    |King     |         6|
 8|Laura     |Callahan |         6|
```
