# AngularJS-Workshop oppgaver

## Lagre tweets lokalt i applikasjonen


- Lag en side med et inputfelt som skal være twitter meldinga. Den skal vises på førstesiden.
- lag et "preview" felt av twittermelding
- lag en knapp som legger til meldinga i et array på $scope.
- gjør knappen &lt;button disabled&gt; hvis inputfeltet er tomt.

## Vise alle tweets

- Lag en html-liste som viser alle tweets.
- Legg på dato på tweet-meldinga, og vis dato på formatet "ddMM H:mm" i tweet lista
- Sorter twitter-meldingene etter dato

## Lag en login-side
- Opprett loginController og login.html med routing i app.js
- Inputfelt brukernavn og passord
- Opprett en brukerService som holder på brukernavn og passord
- Opprett en metode på brukerService som heter login.
 - Denne skal gjøre et httprequest til twitter.lazy.wtf/login (se [server/README.md](server/README.md))
 - Hvis http 200, returner true og bruker er logget inn (lagret i brukerService).

## TwitterService
- opprett en twitterService som injecter brukerService
- lag en metode som lagrer tweet for bruker.
	- $http.post() - brukernavn og passord må med i meldinga, se server/README.md
- lag en metode som henter alle tweets
	- $http.get()
