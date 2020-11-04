# TP2

```sql
-- on crée le serveur "distant", ici vers la base 'pedago'
-- on lève ici les droits d'écritures (que les utilisateurs n'ont pas de toute façon)
CREATE SERVER IF NOT EXISTS ro_local_bd_pedago
  FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host 'bd-pedago.univ-lyon1.fr', port '5432', dbname 'pedago',  updatable 'false');

-- pour annuler
-- DROP SERVER IF EXISTS ro_local_bd_pedago;

--  on dit que l'utilisateur local LoginPostgres accède au distant via le même compte LoginPostgres : il faut préciser le mot de passe
CREATE USER MAPPING IF NOT EXISTS FOR p1704709 SERVER ro_local_bd_pedago OPTIONS (user 'p1704709', password 'mgfk0w0kmOdj');

-- pour annuler
-- DROP USER MAPPING IF EXISTS FOR LoginPostgres SERVER ro_local_bd_pedago;

-- enfin pour ajouter, ici DEUX TABLES DU SCHEMA mif04_xml
IMPORT FOREIGN SCHEMA mif04_xml
  LIMIT TO (arbres_foret_2011, documentation_2011)
  FROM SERVER ro_local_bd_pedago INTO public;

-- on teste
SELECT COUNT(*)
FROM arbres_foret_2011;


-- On créée des vues pour travailler plus confortablement
create view arbres as
select * from arbres_foret_2011;

create view documentation as
select * from documentation_2011;

select * from documentation;
select * from arbres;

select a, htot
from arbres
where idp = 613376
    and htot is not null;

-- Donner, pour chaque arbre de la parcelle 613376 (IDP), sa hauteur totale (HTOT).
select XMLElement(name arbre,
    XMLElement(
        name hauteur, htot
    )) as arbre, a
from arbres
where idp = 613376
    and htot is not null;

-- Reprendre la question précédente et ajouter un attribut id (valeur obtenue via A) dans l’élément arbre.
select XMLElement(name arbre,
    XMLAttributes(a as id),
    XMLElement(
        name hauteur, htot
    )) as arbre, a
from arbres
where idp = 613376
    and htot is not null;

-- Ajouter, lorsqu’elle est disponible, le nom de l’espèce (code: ESPAR, nom obtenu via la vue documentation
select XMLElement(name arbre,
    XMLAttributes(a as id),
    XMLElement(
        name hauteur, htot
    ),XMLElement(
        name espece, libelle
    )) as arbre, a
from arbres a
    left outer join documentation
    on espar = code
    and donnee = 'ESPAR'
where idp = 613376
    and htot is not null;

-- Donner pour chaque espèce (valeur distincte ESPAR) son nom (si disponible) et le nombre d’arbres de cette espece.
select xmlelement(name espece,
    xmlattributes(code),
    xmlelement(
        name nom, libelle
    ), xmlelement(name nombre, (select count(*) from arbres where code = espar)
    )) as especes
from documentation
where donnee = 'ESPAR';


-- Pour chaque parcelle dont l’identifiant (IDP) est inférieur ou égal à 600200,
-- donner l’identifiant de la parcelle
-- et la liste (sans doublons) des espèces présentes dans cette parcelle
-- (son code ESPAR sous forme d’attribut XML
-- et pour celles dont on le connait, leur nom sous forme de texte).
select distinct idp, count(espar), array_agg(espar), array_agg(libelle)
from arbres a
    left outer join documentation
    on espar = code
    and donnee = 'ESPAR'
where idp <= 600200
group by idp;
select idp, count(a), xmlelement(name especes,
    (select xmlelement(name espece, (select libelle
    from arbres a2
        left outer join documentation d2
        on espar = code
        and donnee = 'ESPAR'
    where a.idp = a2.idp))))
from arbres a
    left outer join documentation d
    on espar = code
    and donnee = 'ESPAR'
where idp <= 600200
group by idp;
```
