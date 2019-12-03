# wikidata-reservation
Wikidata Reservation Service

## Installation
```
cd wikidata-reservation
export FLASK_APP=reservation_rest_api.py
flask run
```

## Basic Command
When you use this command, it will return a new qnode under your satellite namespace.

```
curl -d 'namespace=<Your satellite namespace>' http://localhost:5000/reservation 
```
