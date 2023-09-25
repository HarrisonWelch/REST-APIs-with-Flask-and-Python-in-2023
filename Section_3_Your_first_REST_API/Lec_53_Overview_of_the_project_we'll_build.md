# Overview of the project we'll build

Building our first API. Receive requests from mobile app and respond with some data. Benefit is that multiple sources can request and receive.

- Create stores
- Create items within a store
- Get list of all items
- Given its name, retrieve an individual store and all its items.
- Given a store name, get only a list of items within it.

## Create stores

### Request

```
POST /store {"name": "My Store"}
```

### Response

```json
{ "name": "My store", "items": [] }
```

## Create Items

### Request

```
POST /store/My Store/item {"name": "Chair", "price": 175.50}
```

### Response

```json
{ "name": "Chair", "price": 175.5 }
```

May not be important, but this will confirm. Respond with information sent.

## Retrieve all stores and their items

### Request

```
GET /store
```

### Response

```json
{
  "stores": [
    {
      "name": "My Store",
      "items": [
        {
          "name": "Chair",
          "price": 175.5
        }
      ]
    }
  ]
}
```

## Get a particular store

### Request

```
GET /store/My Store
```

### Response

```json
{
  "name": "My Store",
  "items": [
    {
      "name": "Chair",
      "price": 175.5
    }
  ]
}
```

## Get only items in a store

### Request

```
GET /store/My Store/item
```

### Response

```json
[
    {
        "name": "Chair",
        "price": 175.50
    }
]
```
