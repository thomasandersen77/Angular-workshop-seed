all: twitter-mock

twitter-mock:
	docker build -t registry.laat.io/twitter-mock source

install:
	cp *.service /lib/systemd/system

.PHONY: twitter-mock install all
