# Étudiant1 -> Nom : MOLINARES VALENCIA Prénom : Diogenes Numéro : p2019196
# Étudiant2 -> Nom : BUNEL Prénom : Maxime Numéro : p1914012
# Étudiant3 -> Nom : GIRAUD Prénom : Julien Numéro : p1704709

# Ecrivez votre code Python ici ...
# Partie récupération des données
import geojson
import requests
import pg8000.native
from shapely import wkb
import simplekml
import json

antennes = []
con = pg8000.native.Connection("p1914012", password="nBdh3CzPeZYp", database="p1914012")
table = con.run("SELECT * FROM correction")
for line in table:
    # line[5] = wkb.loads(bytes.fromhex(line[5]))
    antennes.append([line[0], [wkb.loads(bytes.fromhex(line[1])).y,wkb.loads(bytes.fromhex(line[1])).x], line[2]])
print(antennes)

# Partie serveur Flask

from flask import Flask
from flask_cors import CORS

app = Flask(name)
CORS(app)


# Sur terminal
# export FLASK_APP=main_2_2
# flask run --port 8010
@app.route("/antennes")
def get_antennes():
    return json.dumps(antennes)












