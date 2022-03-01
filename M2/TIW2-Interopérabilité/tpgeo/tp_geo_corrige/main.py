import requests
import pg8000.native

url = 'http://api.geonames.org/search?&maxRows=10&username=maxime&type=json&orderby=population&featureClass=P&country=FR'
response = requests.get(url).json()

print(response)
try:
    con = pg8000.native.Connection("p1914012", password="nBdh3CzPeZYp", database="p1914012")
    con.run("DROP TABLE cities")
    con.run("CREATE TABLE cities (id_vi INTEGER, nom_vi VARCHAR, geom GEOMETRY)")
except:
    print("table exist")

for city in response["geonames"]:
    print(city)
    con.run("INSERT INTO cities (id_vi, nom_vi, geom) VALUES (:id_vi, :nom_vi, ST_GeomFromText(:geom))",
            id_vi=city["geonameId"],
            nom_vi=city["name"],
            geom="POINT(" + city["lng"] + ' ' + city["lat"] + ")"
            )

