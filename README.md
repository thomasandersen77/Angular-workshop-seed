# AngularJS-Workshop oppgaver

## Lagre tweets lokalt i applikasjonen


- Lag en side med et inputfelt som skal være twitter meldinga. Den skal vises på førstesiden.
- lag et "preview" felt av twittermelding
- lag en knapp som legger til meldinga i et array på $scope og fjerner meldinga fra inputfeltet.
 - [Array.push](http://www.w3schools.com/jsref/jsref_push.asp)
- gjør knappen &lt;button disabled&gt; hvis inputfeltet er tomt.
 - [ngDisabled](https://docs.angularjs.org/api/ng/directive/ngDisabled)

## Vise alle tweets

- Lag en html-liste som viser alle tweets.
 - [ngRepeat](https://docs.angularjs.org/api/ng/directive/ngRepeat)
- Legg på dato på tweet-meldinga, og vis dato på formatet "dd.MM H:mm:ss" i tweet lista
 - [date](https://docs.angularjs.org/api/ng/filter/date)
- Sorter twitter-meldingene etter dato, nyeste øverst.
 - [orderBy](https://docs.angularjs.org/api/ng/filter/orderBy)

## Lag en login-side
- Opprett LoginCtrl og login.html riktig routing i app.js
- Opprett inputfelt brukernavn og passord
- Opprett en brukerService som holder på brukernavn og passord
  - [services](https://docs.angularjs.org/guide/services)
- Opprett en metode på brukerService som heter login.
 - Denne skal gjøre et httprequest til twitter.lazy.wtf/login (se [server/README.md](server/README.md))
 - Hvis http 200, returner true og bruker er logget inn (lagret i brukerService).
 - [angular-di](https://docs.angularjs.org/guide/di) [http](https://docs.angularjs.org/api/ng/service/$http)

## TwitterService
- opprett en twitterService som injecter brukerService
- lag en metode som lagrer tweet for bruker.
	- $http.post() - brukernavn og passord må med i meldinga, se server/README.md
- lag en metode som henter alle tweets
	- $http.get()
