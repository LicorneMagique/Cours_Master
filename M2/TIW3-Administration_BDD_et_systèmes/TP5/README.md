# TP

```shell
# Après avoir téléchargé le répertoir
# cd $rep
for file in $(ls *gz); do gzip -d $file; done


docker exec -it tp5_postgres_1 /bin/bash
cd /home/data
psql -U postgres -d petasky -c "drop table if exists petasky.object, petasky.source"
for file in $(ls *.sql); do psql -U postgres -d petasky < $file; done
for file in $(ls *0*); do psql -U postgres -d petasky -c "COPY petasky.object FROM '/home/data/$file' WITH DELIMITER ',' NULL 'NULL';"; done

```
