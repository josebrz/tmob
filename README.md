# APP tmob

To run the application create a .env file in the root of the project with the following content

```angular2html
APP_PORT=8000
HOST_REDIS=redis
PORT_REDIS=6379

#DATABASE
MYSQL_DATABASE=mysql
MYSQL_USER=mysql
MYSQL_PASSWORD=mysql
DB_PORT=3306
DB_HOST=database

#CORS
CORS=http://localhost:3000,http://localhost

#FUNCTIONALITY
DEBUG=True
STAGE=dev
ENVIRONMENT=DEV
RUN_MIGRATION=True
RUN_COLLECTSTATIC=True
RUN_DUMPS=True

SECRET_KEY='django-insecure-se4iy2cb_15lpwr^_a3@n4@^f6np*y6$mc3u))l17^4sfef4c2'
```

To continue you must have Docker and Docker-compose installed

```
https://docs.docker.com/get-docker/

https://docs.docker.com/compose/install/
```

Then run the command

```angular2html
make up
```

To enter the django admin you must enter [here](http://0.0.0.0:8000/backoffice/)
```
username: test
password: test
```
To see the logs run
```angular2html
make logs
```

To execute test run the following command
```angular2html
make test
```

To finish running the api run
```angular2html
make down
```

for more commands see Makefile file