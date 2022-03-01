-- Étudiant1 -> Nom : MOLINARES VALENCIA Prénom : Diogenes Numéro : p2019196
-- Étudiant2 -> Nom : BUNEL Prénom : Maxime Numéro : p1914012
-- Étudiant3 -> Nom : GIRAUD Prénom : Julien Numéro : p1704709

-- Ecrivez votre requête SQL ici ...

create table correction as (select id, st_translate(geom,-0.5,0) from antennes a);

select * from correction c order by ST_YMax(Box2D(st_translate)) desc;











