# MySite

### Getting started with Django Project
```
django-admin startproject project_name
python manage.py startapp app_name
python manage.py runserver address:port
```

### Setting up MariaDB
##### Install mysqlclient on MAC
Answered by [notFloran on StackOverflow](https://stackoverflow.com/questions/44239393/installing-mysqlclient-for-mariadb-on-mac-os-for-python3)

```
brew install mariadb
brew unlink mariadb

brew install mariadb-connector-c
ln -s /usr/local/opt/mariadb-connector-c/bin/mariadb_config /usr/local/bin/mysql_config

pip install mysqlclient

rm /usr/local/bin/mysql_config
brew unlink mariadb-connector-c
brew link mariadb
```
##### Create/Update MySQL DB
```
Edit mysite/settings.py

76 DATABASES = {
77     'default': {
78         'ENGINE': 'django.db.backends.mysql',
79         'NAME': 'mysite',
80         'USER': 'yourusername',
81         'PASSWORD': 'yourpassword',
82         'HOST': '127.0.0.1',
83         'PORT': '3306',
84     }
85 }

Start MySQL server and create user with privilege

$ mysql -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 10.2.6-MariaDB Homebrew

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create user 'yourusername'@'localhost' IDENTIFIED BY 'yourpassword';
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]> grant all privileges ON * . * TO 'yourusername'@'localhost';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> create database mysite;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> Bye

$mysql -u yourusername -p
Enter password: yourpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 16
Server version: 10.2.6-MariaDB Homebrew

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database mysite;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> Bye
```
```
python manage.py migrate
```
