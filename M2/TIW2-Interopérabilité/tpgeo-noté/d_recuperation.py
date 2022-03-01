# Étudiant1 -> Nom : MOLINARES VALENCIA Prénom : Diogenes Numéro : p2019196
# Étudiant2 -> Nom : BUNEL Prénom : Maxime Numéro : p1914012
# Étudiant3 -> Nom : GIRAUD Prénom : Julien Numéro : p1704709

# Ecrivez votre code Python ici ...
import pg8000.native
from shapely import wkb

con = pg8000.native.Connection("p1914012", password="nBdh3CzPeZYp", database="p1914012")
table = con.run("SELECT * FROM correction")
con.run("ALTER TABLE correction ADD COLUMN IF NOT EXISTS circle geometry")
for line in table:
    line[1] = wkb.loads(bytes.fromhex(line[1]))
    circle = line[1].buffer(50.0)
    con.run("UPDATE correction SET circle = :circle WHERE id=:id", circle=circle, id=line[0])