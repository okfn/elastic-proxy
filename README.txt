Elastic Proxy
-------------

Elastic search over the web.

Provide an authentiction layer on top of elastic search, so it can (more) safely be used over the internet.

It requires nginx, flask and Elastic search of course. nginx example config included.

The aim is to just ask the flask app if its ok to goto that address and if so let the client talk directly to elastic search through nginx. 



