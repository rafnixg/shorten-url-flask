# URL Shortener in Flask
Web service using Flask framework for Shortener URLs

## Install
Create Virtual env
```bash
$ python3 -m venv env
```
Install requirements.txt
```bash
$ source env/bin/activate
$ pip install -r requirements.txt
```
Initializate the DB
```bash
$ flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```
## Run
```bash
$ flask run
```
## Testing using CURL
Create new link
```bash 
$ curl --header "Content-Type: application/json" --request POST --data '{"url":"http://github.com/"}' http://localhost:5000/
```
Get all links

```bash
$ curl --header "Content-Type: application/json" --request GET http://localhost:5000/
```
