import requests
import pg8000.native

url = 'http://api.geonames.org/search?&maxRows=10&username=maxime&type=json&orderby=population&featureClass=P&country=FR'
response = requests.get(url).json()

print(response)
try:
    con = pg8000.native.Connection("user", password="password", database="tiw2")
    con.run("CREATE TABLE cities (id_vi INTEGER, nom_vi VARCHAR, geom GEOMETRY)")
except:
    print("table exist")

for city in response["geonames"]:
    sql = str.format("INSERT INTO cities (id_vi, nom_vi, geom) VALUES ({id_vi}, '{nom_vi}', ST_GeomFromText('POINT({lng} {lat})'))",
        id_vi=city["geonameId"], nom_vi=city["toponymName"], lat=city["lat"], lng=city["lng"])
    print(sql)
    con.run(sql)
    print(city)
