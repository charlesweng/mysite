# MySite
[![Build Status](https://travis-ci.org/charlesweng/mysite.svg?branch=master)](https://travis-ci.org/charlesweng/mysite)

### Requirements
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [Mac OS X](https://www.apple.com/macos/sierra/)
* [MySQL](https://mariadb.com/downloads?utm_campaign=web_download_server&utm_source=google&utm_medium=ppc&gclid=CjwKEAjw7J3KBRCxv93Q3KSukXQSJADzFzVSbc8WGJoA5lefXsn9KgLVg4361hfx85uC21MiC0Un2RoCRB_w_wcB) (MariaDB)
* [Django](https://www.djangoproject.com/)
* [Homebrew](https://brew.sh/)

### Optional
* [asdf-vm](https://github.com/asdf-vm/asdf)
(extendable version manager)
</br>
Hint: Follow [ExperimentsWithCode's post](https://stackoverflow.com/questions/20361073/installed-django-with-pip-django-admin-py-returns-command-not-found-what-am-i) if you get django-admin not found error

### Getting started with Django Project
```
# Create Project
django-admin startproject project_name
# Create App Within Project
python manage.py startapp app_name
# Start Server
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
##### Creates username/password for the mariadb database
```
export HOSTNAME=yourhostname (default: localhost)
export DB_ADMIN=yourmysqldbadmin (default: root)
export DB_ADMIN_PASSWORD=yourmysqladminpassword (default: none)
export DB_USER=yourusername (default: mysiteuser)
export DB_USER_PASSWORD=yourpassword
export DB_NAME=yourdatabasename (default: mysite)
export DB_TYPE=yourdatabasetype (default: mariadb)
python setup.py
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
82         'HOST': 'yourhostname', #(localhost or 127.0.0.1)
83         'PORT': '3306',
84     }
85 }
```
```
# Migrate (update/create) Database With Django's ORM

# Prepares to create/update/delete tables in database
python manage.py makemigrations app_name
# Create snapshot of changes to database
python manage.py sqlmigrate polls 0001
# Applies migration changes to database
python manage.py migrate
```
