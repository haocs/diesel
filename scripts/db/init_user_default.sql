CREATE USER 'default_user'@'localhost'
IDENTIFIED BY 'default_password';

GRANT ALL PRIVILEGES ON *.* TO 'default_user'@'localhost';
FLUSH PRIVILEGES;
