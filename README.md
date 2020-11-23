# Demo Caching Service written in python

A [caching service app](https://github.com/daviddul/python-caching-service/tree/main/server) and a simple [web app](https://github.com/daviddul/python-caching-service/tree/main/client) that connects to and uses the caching service.

## Caching Service App (server)

### Functionality
* Serve client requests through websocket connection
* Store retrieve values with their keys in an internal hash table and support get and set
* Throw away old data with LRU cache eviction policy when the stored data

### The socket server
The app is a [TCP socket server](https://github.com/daviddul/python-caching-service/blob/main/server/socket_server.py), listening to incoming messages. Messages are parsed to parameters such as cache method, key, value and then passed to the cache backend(s). Another choice could be to provide an http api for the service (and a client for it) instead of the socket connection.

### The cache backend(s)

* The service implements caching in the [lru_cache module](https://github.com/daviddul/python-caching-service/tree/main/server/lru_cache), with an in-memory key-value store, using a hash table.
* The service implements an LRU cache eviction policy.
* For the LRU eviction policy, we need to maintain the order of the keys in which they were added to the cache. This can be done by tracking the keys in the hashmap with a doubly linked list.
* In python, there is a built in data structure for this, the `OrderedDict`. However, I wanted to demonstrate the LRU caching algorithm, so there are 2, easily swappable, cache backends, one using the builtin OrderedDict data structure, and the other implementing it with a plain `dict` and a linked list.

## Web app (client)

It's a simple Flask [app](https://github.com/daviddul/python-caching-service/tree/main/client) that serves a HTTP API. Here is how to try it:

 `curl -d "k1=v1" -d "k2=v2" -X POST http://0.0.0.0:5000/api/storage/`

 `curl -X GET http://0.0.0.0:5000/api/storage/\?key\=k1`


The API uses the [cache_client](https://github.com/daviddul/python-caching-service/tree/main/client/cache_client) module to communicate with the cache service through a socket connection.

## Installation locally

Requirements: [download and install Docker](https://docs.docker.com/get-docker/).

```
docker-compose up --build
```

## Running the app locally

```
docker-compose up
```

## Debugging and testing locally

```
docker-compose exec client sh
docker-compose exec client nose2 --verbose

docker-compose exec server sh
docker-compose exec server nose2 --verbose
```
