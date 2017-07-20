"""
Problem:
Imagine that the most commonly used ORM framework for django does not support the
database you need and third-party ORMs are too buggy stages to use or still in their
experimental stages.

Goal:
The purpose of this script is to setup the database without relying on any sql client:

Hopefully in the future, I can extend this to include setting up different types of databases
(e.g. Postgres, Redis, MongoDB, ElasticSearch, HBase, Cassandra)

Also, hopefully in the future, I can provide the clean up scripts for this setup.

NOTES:
I hate PEP8's 4 tab spaces policy so I use 2 spaces for tab. If adhering to PEP8 is
extremely important, I apologize.

Originally each class are in each of their own files, but I have mreged them into one
so it is easier to transfer. Also, they had doctest but removed to simplify reading.
"""
from functools import partial
import logging
import logging.config
import os
import subprocess


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('dbSetup')


HOSTNAME = os.getenv('HOSTNAME', 'localhost')
DB_ADMIN = os.getenv('DB_ADMIN', 'root')
DB_ADMIN_PASSWORD = os.getenv('DB_ADMIN_PASSWORD', None)
DB_USER = os.getenv('DB_USER', 'mysiteuser')
DB_USER_PASSWORD = os.getenv('DB_USER_PASSWORD')
DB_NAME = os.getenv('DB_NAME', 'mysite')
DB_DIRECTORY = os.getenv('DB_DIRECTORY', '/usr/local/pgsql/data')
DB_TYPE = os.getenv('DB_TYPE', 'mariadb')


class MariaDB:


  def __init__(self, admin, admin_password, hostname):
    self.admin = admin
    self.admin_password = admin_password
    self.hostname = hostname


  def start_server(self):
    start_mysql_server_result = subprocess.getoutput(['mysql.server restart'])
    logger.debug(start_mysql_server_result)

  def create_user(self, user, user_password):
    CREATE_USER_QUERY = "CREATE USER '{}'@'{}' IDENTIFIED BY '{}';"\
                                  .format(user, self.hostname, user_password)
    self.run_query(CREATE_USER_QUERY, self.admin)


  # TODO need to grant only the privileges that the user needs for this app
  def grant_all_privileges(self, user):
    GRANT_PRIVILEGES_QUERY = "GRANT ALL PRIVILEGES ON * . * TO '{}'@'{}';"\
                                      .format(user, self.hostname)
    RELOAD_PRIVILEGES_QUERY = "FLUSH PRIVILEGES;"
    self.run_query(GRANT_PRIVILEGES_QUERY, self.admin, self.admin_password)
    self.run_query(RELOAD_PRIVILEGES_QUERY, self.admin, self.admin_password)


  def create_database(self, username, password, database_name):
    CREATE_DATABASE_QUERY = "CREATE DATABASE " + database_name + ";"
    self.run_query(CREATE_DATABASE_QUERY, username, password)


  # TODO:: need to fix duplicate logging statements
  def run_query(self, query, username, password=None):
    if password:
        db_query_command = 'mysql -u ' + username + ' -p' + password + ' -e ' + '"' + query + '"'
    else:
        db_query_command = 'mysql -u ' + username + ' -e ' + '"' + query + '"'#['mysql', '-u', username, '-e', query]
    query_result = subprocess.getoutput(db_query_command)
    logger.debug(query_result if query_result.strip() != '' else db_query_command)


class Postgres:


  def __init__(self, admin, admin_password, hostname):
    self.admin = admin
    self.admin_password = admin_password
    self.hostname = hostname


  def initdb(self, directory):
    logger.debug('creating directory for postgres database in {}', directory)
    mkdir_result = subprocess.getoutput('mkdir -p ' + directory)
    if mkdir_result.strip() != '':
      logger.debug(mkdir_result)
    initdb_result = subprocess.getoutput('initdb --pgdata ' + directory)
    logger.debug(initdb_result)

  def start_server(self, directory):
    self.initdb(directory)
    logger.debug('starting postgres server in {}', directory)
    start_server_result = subprocess.getoutput('pg_ctl -D ' + directory + ' -l logfile start')
    logger.debug(start_server_result)

  # TODO CREATE ROLE
  def create_user(self, user, user_password):
    pass


  # TODO GRANT PRIVILEGES
  def grant_all_privileges(self, user):
    pass


  # TODO CREATE DATABASE
  def create_database(self, username, password, database_name):
    pass


  # TODO postgres -u postgres ....
  def run_query(self, query, username, password=None):
    pass

# Could have used Abstract Class (ABCMeta, but why not take advantage of functional libraries)
# Nowadays, people just past functions around - even Java 8 uses the Supplier class (lambda constructor)
def Database(db_type = DB_TYPE):
  if db_type.lower() == 'mariadb':
    return partial(MariaDB, DB_ADMIN, DB_ADMIN_PASSWORD, HOSTNAME)
  elif db_type.lower() == 'postgres':
    return partial(Postgres, DB_ADMIN, DB_ADMIN_PASSWORD, HOSTNAME)


def setup_database():
  my_database = Database(DB_TYPE)()
  my_database.start_server(DB_DIRECTORY)
  my_database.create_user(DB_USER, DB_USER_PASSWORD)
  my_database.grant_all_privileges(DB_USER)
  my_database.create_database(DB_USER, DB_USER_PASSWORD, DB_NAME)


def main():
  setup_database()


if __name__ == '__main__':
  main()
