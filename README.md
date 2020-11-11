
TRAILLER PLAN API
======================

This project is an sample of rest api using flask, with docker or not.
run the rest api under root dir of the project : 

```shell script
$ python src/user/UserModule.py
```

####Test 1 -- GET users
```shell script
$ curl http://localhost:5000/trailerplan/api/v1.0/users

$ [{"id":0,"firstName":"Kilian","lastName":"Jornet","sexe":"masculin","birthday":"1987-10-27","address":{"id":0,"city":"Sabadell","country":"Espagne"},"civility":"Monsieur"},{"id":1,"firstName":"Sebastien","lastName":"Chaigneau","sexe":"masculin","birthday":"1972-02-23","address":{"id":1,"city":"Châtellerault","country":"France"},"civility":"Monsieur"},{"id":2,"firstName":"Caroline","lastName":"Chaverot","sexe":"féminin","birthday":"1976-10-16","address":{"id":2,"city":"Genève","country":"Suisse"},"civility":"Madame"},{"id":3,"firstName":"Eric","lastName":"Clavery","sexe":"masculin","birthday":"1980-06-07","address":{"id":3,"city":"Coutances","country":"France"},"civility":"Monsieur"},{"id":4,"firstName":"François","lastName":"Delabarre","sexe":"masculin","birthday":"1968-01-03","address":{"id":4,"city":"Lille","country":"France"},"civility":"Monsieur"},{"id":5,"firstName":"Corinne","lastName":"Favre","sexe":"féminin","birthday":"1970-12-15","address":{"id":5,"city":"Chambéry","country":"France"},"civility":"Madame"},{"id":6,"firstName":"Emilie","lastName":"Forsberg","sexe":"féminin","birthday":"1986-12-11","address":{"id":6,"city":"Sollefteå","country":"Suède"},"civility":"Madame"},{"id":7,"firstName":"Anna","lastName":"Frost","sexe":"féminin","birthday":"1981-11-01","address":{"id":7,"city":"Dunedin","country":"Nouvelle-Zélande"},"civility":"Madame"},{"id":8,"firstName":"Maud","lastName":"Gobert","sexe":"féminin","birthday":"1977-04-25","address":{"id":8,"city":null,"country":"France"},"civility":"Madame"},{"id":9,"firstName":"Antoine","lastName":"Guillon","sexe":"masculin","birthday":"1970-06-16","address":{"id":9,"city":"Yvelines","country":"France"},"civility":"Monsieur"},{"id":10,"firstName":"Scott","lastName":"Jurek","sexe":"masculin","birthday":"1973-10-26","address":{"id":10,"city":"Duluth","country":"Etats-Unis"},"civility":"Monsieur"},{"id":11,"firstName":"Anton","lastName":"Krupicka","sexe":"masculin","birthday":"1983-08-08","address":{"id":11,"city":"Nebraska","country":"Etats-Unis"},"civility":"Monsieur"},{"id":12,"firstName":"Nathalie","lastName":"Mauclair","sexe":"féminin","birthday":"1970-05-09","address":{"id":12,"city":null,"country":"France"},"civility":"Madame"},{"id":13,"firstName":"Dawa","lastName":"Dachhiri Sherpa","sexe":"masculin","birthday":"1969-11-03","address":{"id":13,"city":"Taksindu Solukumbu","country":"Népal"},"civility":"Monsieur"},{"id":14,"firstName":"Xavier","lastName":"Thévenard","sexe":"masculin","birthday":"1988-03-06","address":{"id":14,"city":"Nantua","country":"France"},"civility":"Monsieur"}]
```

####Test 2 -- GET user by id
```shell script
$ curl http://localhost:5000/trailerplan/api/v1.0/user/0

$ {"id":0,"firstName":"Kilian","lastName":"Jornet","sexe":"masculin","birthday":"1987-10-27","address":{"id":0,"city":"Sabadell","country":"Espagne"},"civility":"Monsieur"}
```
with more details put option -v : 
```shell script
$ curl http://localhost:5000/trailerplan/api/v1.0/users/0 -v

*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 5000 (#0)
> GET /trailerplan/api/v1.0/users/0 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 170
< Server: Werkzeug/1.0.1 Python/3.7.9
< Date: Wed, 11 Nov 2020 16:07:43 GMT
< 
* Closing connection 0
{"id":0,"firstName":"Kilian","lastName":"Jornet","sexe":"masculin","birthday":"1987-10-27","address":{"id":0,"city":"Sabadell","country":"Espagne"},"civility":"Monsieur"}
$
```

####Test 3 -- POST create an user
```shell script
$ curl -X POST -H "Content-Type: application/json" -d '{"firstName":"KilianNew","lastName":"JornetNew","sexe":"masculin","birthday":"1987-10-27","adresse":{"city":"Sabadell","country":"Espagne"},"civilite":"Monsieur"}'  http://localhost:5000/trailerplan/api/v1.0/users

{"firstName":"KilianNew","lastName":"JornetNew","sexe":"masculin","birthday":"1987-10-27","adresse":{"city":"Sabadell","country":"Espagne","id":15},"civilite":"Monsieur","id":15}
```

####Test 4 -- PUT update an user
```shell script
$ curl -X PUT -H "Content-Type: application/json" -d '{"id":15,"firstName":"KilianUpdate","lastName":"JornetUpdate","sexe":"masculinUpdate","birthday":"1987-10-27","adresse":{"id":15,"city":"Sabadell","country":"Espagne"},"civilite":"Monsieur"}'  http://localhost:5000/trailerplan/api/v1.0/users/15

{"id":15,"firstName":"KilianUpdate","lastName":"JornetUpdate","sexe":"masculinUpdate","birthday":"1987-10-27","adresse":{"id":15,"city":"Sabadell","country":"Espagne"},"civilite":"Monsieur"}
```

####Test 5 -- DELETE delete an user
get the user with is 15, delete it, check that it deleted, done!

```shell script
$ curl http://localhost:5000/trailerplan/api/v1.0/users/15
{"id":15,"firstName":"KilianUpdate","lastName":"JornetUpdate","sexe":"masculinUpdate","birthday":"1987-10-27","adresse":{"id":15,"city":"Sabadell","country":"Espagne"},"civilite":"Monsieur"}

$ curl -X DELETE http://localhost:5000/trailerplan/api/v1.0/users/15
{"id":15,"firstName":"KilianUpdate","lastName":"JornetUpdate","sexe":"masculinUpdate","birthday":"1987-10-27","adresse":{"id":15,"city":"Sabadell","country":"Espagne"},"civilite":"Monsieur"}

$ curl http://localhost:5000/trailerplan/api/v1.0/users/15
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```  

The test data are in the list of User. They are some few ultra trailers (my favorite sports :-) ).

####1. Object model and DAO
It is a classic User (id, firstname, lastname, sexe, birthday, short address (id, city, country), civility).
The address and abstract class are for future usage.
The DAO can access to the data in the table by reading, writing and deleting.

####2. Controller
It is the rest API using flask. The controller managed few error status code like 404 or 400.
The entry data are tested.

####3. Containerisation
pull the image python:3.7.9.

```shell script
$ docker pull python:3.7.9 
```

Docker file :
```text
FROM python:3.7.9  
MAINTAINER boonsuli@gmail.com  
WORKDIR /app    
COPY ./requirements.txt /app/requirements.txt  
RUN pip install -r requirements.txt  
COPY src /app  
CMD [ "python", "./user/UserModule.py" ]  
```

Build :
```shell script
$ docker build -t trailerplan .
```

Run :
```shell script
$ docker run -id -p 5000:5000 trailerplan
```

To check inside the container with bash :
```shell script
$ docker run -it trailerplan /bin/bash
```

####4. References
[flask](https://flask.palletsprojects.com/en/1.1.x/)
[flask-api](https://github.com/flask-api/flask-api)
[munch](https://github.com/Infinidat/munch)
[orjson](https://github.com/ijl/orjson)
