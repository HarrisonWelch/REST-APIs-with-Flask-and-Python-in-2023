# How to get a specific store and its items

Picking up from last lecture

Make endpoints for getting store by name and getting items in the store by name.

```py
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]} # Dict for extensibility later, more keys doesn't hurt anything unlike changing data type
    return {"message": "Store not found"}, 404
```

Test get store by name:

![60_test_get_store_by_name image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/60_test_get_store_by_name.png)

Test get store items by name:

![60_test_get_items_in_store_by_name image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/60_test_get_items_in_store_by_name.png)

Automated tests on everything we run. GitHub has some auto-tests for view and using.
