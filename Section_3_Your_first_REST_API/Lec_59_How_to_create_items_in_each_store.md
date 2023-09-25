# How to create items in each store

Continuing from last lecture app.py.

Lets say we want the URL to be something like: http://127.0.0.1:5000/store/My Store

Lets make a path to grabe the "My Store" out of a URL

```py
@app.post("/store/<string:name>")
def create_item(name):
    pass

```

You can also use std URL queries like `...?name=My Store`

Can also add to headers, but nobody does that

Let's finish the endpoint in python

```py

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
```

If we can't find the store return 404 with that message else update the right store with the right item. Don't worry about duplicate store names for now.

Testing the create item for store

![59_stores_after_add_item image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/59_stores_after_add_item.png)

Test get all stores to see if the item is there and it is.

Now create a new store, add a new item and test if it exists in the new store.

Crate store

![59_create_store_2 image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/59_create_store_2.png)

Create item

![59_create_laptop_in_store_2 image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/59_create_laptop_in_store_2.png)

View all stores

![59_store_after_add_item_in_store_2 image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/59_store_after_add_item_in_store_2.png)

All works!
