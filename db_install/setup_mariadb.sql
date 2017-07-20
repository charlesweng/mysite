CREATE USER 'mysiteuser'@'localhost' IDENTIFIED BY 'mysiteuser';
GRANT ALL PRIVILEGES ON *.* TO 'mysiteuser'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE mysite;
