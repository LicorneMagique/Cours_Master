import pg8000.native
from shapely import wkb

con = pg8000.native.Connection("user", password="password", database="tiw2")
table = con.run("select * from meteo_e_villes_aero")
print(table)

for line in table:
    line[5] = wkb.loads(bytes.fromhex(line[5]))
print(table)

icaos = {line[4] for line in table}

result = {"properties": []}
for line in table:
    data = {"geometry": todo, "properties": {"aeroport": line[2], "distance": line[0], "icao": line[4], "id_va": line[3], "ville": line[1]}}
    result.properties.append()

print(1)