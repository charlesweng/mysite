import os
import subprocess

HOSTNAME = os.getenv('HOSTNAME', 'localhost')
MARIADB_ADMIN = os.getenv('MARIDADB_ADMIN', 'root')
MARIADB_ADMIN_PASSWORD = os.getenv('MARIDADB_ADMIN_PASSWORD', '')
MARIADB_USER = os.getenv('MARIADB_USER', 'mysiteuser')
MARIADB_USER_PASSWORD = os.getenv('MARIADB_USER_PASSWORD')

def create_user(username=MARIADB_USER, password=MARIADB_USER_PASSWORD, hostname=HOSTNAME, 
    admin_username=MARIADB_ADMIN, admin_password=MARIADB_ADMIN_PASSWORD):

  if password is None or len(password) == 0:
    raise ValueError('password for user' + username + ' is either null or empty')
  
  CREATE_USER_QUERY = "CREATE USER '{}'@'{}' IDENTIFIED BY '{}';".format(username, hostname, password) 

  if admin_password is None:
    admin_password = ''
  else:    
    admin_password = " '-p" + admin_password + "'"

  CREATE_USER_COMMAND = ['mysql', '-u', admin_username,'-e', CREATE_USER_QUERY]
  subprocess.run(CREATE_USER_COMMAND, stdout=subprocess.PIPE)

# TODO need to grant only the privileges that the user needs for this app
def grant_all_privileges(username=MARIADB_USER, hostname=HOSTNAME,
    admin_username=MARIADB_ADMIN, admin_password=MARIADB_ADMIN_PASSWORD):

  GRANT_PRIVILEGES_QUERY = "GRANT ALL PRIVILEGES ON * . * TO '{}'@'{}';".format(username, hostname)
  RELOAD_PRIVILEGES_QUERY = "FLUSH PRIVILEGES;"

  if admin_password is None:
    admin_password = ''
  else:    
    admin_password = " '-p" + admin_password + "'"

  GRANT_PRIVILEGES_COMMAND = ['mysql', '-u', admin_username, '-e', GRANT_PRIVILEGES_QUERY]
  RELOAD_PRIVILEGES_COMMAND = ['mysql', '-u', admin_username, '-e', RELOAD_PRIVILEGES_QUERY]  
  subprocess.run(GRANT_PRIVILEGES_COMMAND, stdout=subprocess.PIPE)
  subprocess.run(RELOAD_PRIVILEGES_COMMAND, stdout=subprocess.PIPE) 

def setup_database():
  create_user()
  grant_all_privileges()

def main():
  setup_database()

if __name__ == '__main__':
  main()
