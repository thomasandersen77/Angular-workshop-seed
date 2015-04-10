#Simple twitter api

## Installing
```
$ mkvirtualenv angular-kurs # optional
$ pip install -r requirements.txt  # legg til --user etter install om du ikke har root
$ python api.py
```

## Getting all tweets
```bash
$ curl -i http://twitter.lazy.wtf/api/v1/tweets
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 271
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: HEAD, GET, POST, OPTIONS
Access-Control-Max-Age: 21600
Access-Control-Allow-Headers: Accept, Origin, Content-Type, X-Requested-With
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.3
Date: Mon, 16 Sep 2013 09:09:52 GMT

{
  "tweets": [
    {
      "text": "first!",
      "timestamp": "2013-09-15T20:48:36.373712",
      "username": "james"
    },
    {
      "text": "@james firsts are stupid..",
      "timestamp": "2013-09-15T20:48:36.373768",
      "username": "douglas"
    }
  ]
}
```

## Getting all tweets by james
```bash
$ curl -i http://twitter.lazy.wtf/api/v1/tweets/james
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 134
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: HEAD, OPTIONS, GET
Access-Control-Max-Age: 21600
Access-Control-Allow-Headers: Accept, Origin, Content-Type, X-Requested-With
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.3
Date: Mon, 16 Sep 2013 09:10:37 GMT

{
  "tweets": [
    {
      "text": "first!",
      "timestamp": "2013-09-15T20:48:36.373712",
      "username": "james"
    }
  ]
}
```


## Getting all users
```bash
$ curl -i http://twitter.lazy.wtf/api/v1/users
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 171
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: HEAD, GET, POST, OPTIONS
Access-Control-Max-Age: 21600
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.3
Date: Sun, 15 Sep 2013 16:04:10 GMT

{
  "users": [
    {
      "full_name": "James Ward",
      "username": "james"
    },
    {
      "full_name": "Doublas Scott",
      "username": "douglas"
    }
  ]
}
```

## registrering av nye brukere
Gjøres ved å poste følgende jsondata til `/api/v1/users
```javascript
{
  "user": {
    "username": "george",
    "password": "password",
    "full_name": "George Bush"
  }
}
```

```bash
$ curl -X POST -i -H "Content-Type:application/json" \
-H "Accept:application/json" http://twitter.lazy.wtf/api/v1/users \
-d '{"user": {"username": "george", "password": "password", "full_name":"George Bush"}}'
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 19
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: HEAD, GET, POST, OPTIONS
Access-Control-Max-Age: 21600
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.5+
Date: Sun, 15 Sep 2013 18:09:25 GMT

{
  "status": 200
}
```

## ny tweet
Gjøres ved å poste følgende jsondata til `/api/v1/tweets`
```javascript
{
  "user": {
    "username": "james",
    "password": "password"
  },
  "text": "dette er en tekst"
}
```

```bash
$ curl -X POST -i -H "Content-Type:application/json" \
-H "Accept:application/json" http://twitter.lazy.wtf/api/v1/tweets \
-d '{"user": {"username": "james", "password": "password"}, "text":"a tweet text"}'
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 98
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: HEAD, GET, POST, OPTIONS
Access-Control-Max-Age: 21600
Access-Control-Allow-Headers: Accept, Origin, Content-Type, X-Requested-With
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.3
Date: Mon, 16 Sep 2013 09:16:29 GMT

{
  "text": "a tweet text",
  "timestamp": "2013-09-16T11:16:29.293807",
  "username": "james"
}
```


## checking username and password
```bash
$ curl -X POST -i -H "Content-Type:application/json" \
-H "Accept:application/json" http://twitter.lazy.wtf/api/v1/login \
-d '{"user": {"username": "james", "password": "password"}}'
```

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 19
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Max-Age: 21600
XSRF-TOKEN: hereBeRandomXSRFtoken
Server: Werkzeug/0.9.4 Python/2.7.5+
Date: Sun, 15 Sep 2013 18:11:39 GMT

{
  "status": 200
}
```
