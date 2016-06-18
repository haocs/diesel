CREATE USER 'dev_user'@'localhost'
IDENTIFIED BY 'dev_password';

GRANT ALL PRIVILEGES ON *.* TO 'dev_user'@'localhost';
FLUSH PRIVILEGES;
