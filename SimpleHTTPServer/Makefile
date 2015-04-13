all: default

build: Main.java
	mkdir -p build/META-INF/
	javac -d ./build Main.java
	cp mime.types build/META-INF

default: build
	cd build && jar cfe SimpleHTTPServer.jar Main *

install:
	cp build/SimpleHTTPServer.jar ../

clean:
	rm -rf build/

.PHONY: install clean
