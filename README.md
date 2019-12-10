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
>>> curl -d 'namespace=<YOUR_SATELLITE_NAMESPACE>' -d 'uri=<YOUR_SATELLITE_URI>' -d 'prefix=<PREFIX_OF_QNODES>' -d 'num_of_0=<NUMBER_OF_0s_BEFORE_QNODE_NUMBER>' http://localhost:5000/register 
Register successfully and you are ready to use this satellite. %
```

To get the information of a satellite:

```
>>> curl http://localhost:5000/<YOUR_SATELLITE_NAMESPACE>
+-------------+-------------------------------+-----------------------+----------+------------+
| Satellite   | Satellite URI                 |   Latest qnode number | Prefix   |   num_of_0 |
|-------------+-------------------------------+-----------------------+----------+------------|
| dm          | https://w3id.org/satellite/dm |                     1 | SDQ      |          6 |
+-------------+-------------------------------+-----------------------+----------+------------+
```

To get the information of all satellites:
```
>>> curl http://localhost:5000/all
+-------------+-------------------------------+-----------------------+----------+------------+
| Satellite   | Satellite URI                 |   Latest qnode number | Prefix   |   num_of_0 |
|-------------+-------------------------------+-----------------------+----------+------------|
| dm          | https://w3id.org/satellite/dm |                     1 | SDQ      |          6 |
+-------------+-------------------------------+-----------------------+----------+------------+
```

To reserve a qnode in a satellite:

```
>>> curl http://localhost:5000/<YOUR_SATELLITE_NAMESPACE>/reservation
{
  "Latest qnode": "SDQ000001"
}% 
```
