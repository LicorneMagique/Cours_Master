-- Création de la base
drop table if exists projet;
create table projet (
    "Programme (2016)" integer,
    "SIREN" varchar(100),
    "NIC" varchar(100),
    "Dénomination" varchar(200),
    "Montant" varchar(100),
    "Objet" varchar(800),
    "Parlementaire" varchar(300),
    "Réserve 2016" varchar(300),
    "Convention 2016" varchar(1500),
    "COG : code département" varchar(100),
    "COG : code commune" varchar(100),
    "COG : ville ou pays" varchar(100),
    "Nomenclature juridique" varchar(100),
    "Code NAF" varchar(100),
    "Situation SIRENE" varchar(300),
    "RNA" varchar(100)
);

-- Chargement des données
-- Updated Rows: 56497
copy projet from '/home/data/projet-de-loi-de-finances-pour-2018-plf-2018-donnees-de-lannexe-jaune-effort-fin.csv' delimiter ';' csv header;

-- Correctif 1.3
-- Updated Rows: 320
update projet set "SIREN" = null where "SIREN" not similar to '(0|1|2|3|4|5|6|7|8|9){9}';

-- Correctif 2.3
-- Updated Rows: 6
update projet set "NIC" = null where "SIREN" is not null and "NIC" not similar to '(0|1|2|3|4|5|6|7|8|9){5}';

-- Correctif 3.3
-- Updated Rows: 10
delete from projet where "SIREN" is not null and "NIC" is null;

-- Correctif 4.3
-- Updated Rows: 5767
update projet set "Situation SIRENE" = null where "Situation SIRENE" is not null and "NIC" is not null;

-- Correctif 5.3
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
