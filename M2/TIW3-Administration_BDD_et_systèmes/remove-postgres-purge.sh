# purge postgres

sudo apt-get --purge remove postgresql\* -y && sudo rm -r /etc/postgresql/ && sudo rm -r /etc/postgresql-common/ && sudo rm -r /var/lib/postgresql/ && sudo userdel -r postgres && sudo groupdel postgres
