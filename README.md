# diesel
Django powered personal website

## Features(TODO)
* [ ] Blog as an app with DB
* [ ] Rate limit
* [ ] UI
* [ ] Logging and debuging
* [ ] Dockerize
* [ ] test

## Requirements
* python: 3.3+
* django: 1.9
* mysql/mariadb

## Setup
* Create DB and DB user [settings](https://github.com/haocs/diesel/blob/master/diesel/settings.py)
* Or running db setup scirpts:
```bash
mysql -uroot -ppasswd < ./scripts/db/init_user_default.sql
mysql -uroot -ppasswd < ./scripts/db/init_db_default.sql
```
* Install dependencies
```bash
# mysql client
sudo apt-get install libmysqlclient-dev # mysql
sudo apt-get install libmariadbclient-dev # mariaDB

sudo zypper install ibmysqlclient-devel # mysql/mariaDB on opensuse

# python-dev 
sudo apt-get install python-dev # ubuntu
sudo zypper install python-devel # opensuse
```
* Install django and other requirements
```bash
# use pip for python3 and virutalenv(optional)
pip install -r requirements.txt
```

### Start
* Run `./manage.py`

