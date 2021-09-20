# URL Shortener in Flask
Web service using Flask framework for Shortener URLs

## Testing using CURL

### Create new link

```bash 
$ curl --header "Content-Type: application/json" --request POST --data '{"url":"http://github.com/"}' http://localhost:5000/
```

### Get all links

```bash
$ curl --header "Content-Type: application/json" --request GET http://localhost:5000/
```
