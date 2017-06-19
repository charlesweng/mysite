# MySite
[![Build Status](https://travis-ci.org/charlesweng/mysite.svg?branch=master)](https://travis-ci.org/charlesweng/mysite)

</br>
### Requirements
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [Mac OS X](https://www.apple.com/macos/sierra/)
* [MySQL](https://mariadb.com/downloads?utm_campaign=web_download_server&utm_source=google&utm_medium=ppc&gclid=CjwKEAjw7J3KBRCxv93Q3KSukXQSJADzFzVSbc8WGJoA5lefXsn9KgLVg4361hfx85uC21MiC0Un2RoCRB_w_wcB) (MariaDB)
* [Django](https://www.djangoproject.com/)
* [Homebrew](https://brew.sh/)

### Optional
* [asdf-vm](https://github.com/asdf-vm/asdf)
(extendable version manager)

### Getting started with Django Project
```
# Create Project
django-admin startproject project_name
# Create App Within Project
python manage.py startapp app_name
# Start Server
python manage.py runserver address:port
# Create snapshot of changes to database
python manage.py makemigrations app_name
# Applies migration changes to database
python manage.py migrate
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
79         'NAME': 'yourdatabasename',
80         'USER': 'yourusername',
81         'PASSWORD': 'yourpassword',
82         'HOST': '127.0.0.1',
83         'PORT': '3306',
84     }
85 }
```
```
Start MySQL server and create user with privilege

$ mysql.server start

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
```
```
Create database with the name you specified in `NAME:yourdatabasename` field in settings.py

$ mysql -u yourusername -p
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
Migrate (update/create) Database With Django's ORM

python manage.py migrate
```
