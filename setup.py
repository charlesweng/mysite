"""
The purpose of this script is to setup the database without relying on any sql client:

Hopefully in the future, I can extend this to include setting up different types of databases
(e.g. Postgres, Redis, MongoDB, ElasticSearch, HBase, Cassandra)
"""
import os
import subprocess

HOSTNAME = os.getenv('HOSTNAME', 'localhost')
MARIADB_ADMIN = os.getenv('MARIADB_ADMIN', 'root')
MARIADB_ADMIN_PASSWORD = os.getenv('MARIADB_ADMIN_PASSWORD', None)
MARIADB_USER = os.getenv('MARIADB_USER', 'mysiteuser')
MARIADB_USER_PASSWORD = os.getenv('MARIADB_USER_PASSWORD')
MYSITE_DATABASE_NAME = os.getenv('MYSITE_DATABASE_NAME', 'mysite')

# DB Query Constants
CREATE_USER_QUERY = "CREATE USER '{}'@'{}' IDENTIFIED BY '{}';".format(MARIADB_USER, HOSTNAME, MARIADB_USER_PASSWORD)
# TODO need to grant only the privileges that the user needs for this app
GRANT_PRIVILEGES_QUERY = "GRANT ALL PRIVILEGES ON * . * TO '{}'@'{}';".format(MARIADB_USER, HOSTNAME)
RELOAD_PRIVILEGES_QUERY = "FLUSH PRIVILEGES;"
CREATE_DATABASE_QUERY = "CREATE DATABASE " + MYSITE_DATABASE_NAME + ";"

def create_user(admin_username=MARIADB_ADMIN, admin_password=None):
  run_query(CREATE_USER_QUERY, admin_username, admin_password)


# TODO need to grant only the privileges that the user needs for this app
def grant_all_privileges(admin_username=MARIADB_ADMIN, admin_password=None):
  run_query(GRANT_PRIVILEGES_QUERY, admin_username, admin_password)
  run_query(RELOAD_PRIVILEGES_QUERY, admin_username, admin_password)


def create_database(username=MARIADB_USER, password=MARIADB_USER_PASSWORD):
  run_query(CREATE_DATABASE_QUERY, username, password)


def run_query(query, username=MARIADB_USER, password=None):
  if password:
      db_query_command = ['mysql', '-u', username, '-p' + password, '-e', query]
  else:
      db_query_command = ['mysql', '-u', username, '-e', query]
  subprocess.run(db_query_command, stdout=subprocess.PIPE)


def setup_database():
  create_user()
  grant_all_privileges()
  create_database()


def main():
  setup_database()


if __name__ == '__main__':
  main()
