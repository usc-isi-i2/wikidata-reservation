# wikidata-reservation
Wikidata Reservation Service

## Prerequisites

* Python 3.6+

## Installation

1. Clone the repository
2. Run:
    ```
    cd wikidata-reservation
    pip install -r requirements.txt
    python reservation_rest_api.py
    ```
3. Server is running at [`http://localhost:5000/`](http://localhost:5000/)


## Call from CURL

To register a satellite:

```
>>> curl -d 'namespace=<YOUR_SATELLITE_NAMESPACE>' -d 'uri=<YOUR_SATELLITE_URI>' http://localhost:5000/register 
Register successfully and you are ready to use this satellite. %
```

To get reservation service table:

```
>>> curl http://localhost:5000/
+-------------+-------------------------------+----------------+
| Satellite   | Satellite URI                 |   Latest qnode |
|-------------+-------------------------------+----------------|
| dm          | https://w3id.org/satellite/dm |              1 |
+-------------+-------------------------------+----------------+%
```

To reserve a qnode:

```
>>> curl -d 'namespace=<YOUR_SATELLITE_NAMESPACE>' http://localhost:5000/reservation
{
    "Latest qnode": "Q000001"
}%
```
