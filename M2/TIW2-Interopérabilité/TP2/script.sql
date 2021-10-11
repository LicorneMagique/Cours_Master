-- Création de la base
DROP TABLE IF EXISTS projet;
CREATE table projet (
    "Programme (2016)" varchar(100),
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

-- Adresse du fichier à mettre à jour par l'utilisateur du script
copy projet from '/home/data/projet-de-loi-de-finances-pour-2018-plf-2018-donnees-de-lannexe-jaune-effort-fin.csv' delimiter ';' csv header;
