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
79         'NAME': os.path.join(BASE_DIR, 'mysite'),
80         'USER': 'yourusername',
81         'PASSWORD': 'yourpassword',
82         'HOST': '127.0.0.1',
83         'PORT': '3306',
84     }
85 }
```
```
python manage.py migrate
```
