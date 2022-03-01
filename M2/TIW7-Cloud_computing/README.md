# Cloud computing

[Cours officieux](http://perso.univ-lyon1.fr/fabien.rico/site/cloud:2020:start)
[Cours officiel](http://perso.univ-lyon1.fr/jean-patrick.gelas/UE_Cloud_CCI/)

## Notes

<http://cloud-info.univ-lyon1.fr/horizon>

## TP1

mdp clé ssh : `toto`

ip : `192.168.166.206`

mdp ubuntu : `1234`

pour filtrer le ssh `not port 22`

pour filtrer avec l'ip `ip.addr == 192.168.166.206`

## TP2

Même clé ssh

ip : `192.168.166.19`

```shell
docker pull mysql:5.7.27
docker run --name dockertest -e MYSQL_HOSTNAME=test -e MYSQL_ROOT_PASSWORD=1234 -d mysql:5.7.27
docker inspect dockertest
docker exec -it dockertest mysql -u root -p1234 --protocol=tcp
docker exec -it dockertest /bin/bash
echo coucou > /toto
exit
flemme
docker run --name dockmysql -v /home/ubuntu/docker/datatest:/var/lib/mysql -e MYSQL_HOSTNAME=mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7.27
ls /home/ubuntu/docker/datatest/
docker exec -it dockmysql mysql -u root -ppassword -e 'CREATE DATABASE BASE_A;'
ls /home/ubuntu/docker/datatest/
# Apparition du dossier BASE_A
```
