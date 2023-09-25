# How to create stores in our REST API

Important to always be insomnia testing your app

If we straight up just hit `http://127.0.0.1:5000/store`

we get an error 405 URL not allowd

![58_405_error_init image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/58_405_error_init.png)

Lets add the endpoint

```py
...
@app.post("/store")
def create_store():
    pass

```

This will cause a 500 b/c of 
```
TypeError: The view function for 'create_store' did not return a valid response. The function either returned None or ended without a return statement.
```

as described in the flask error out

![58_500_error_did_not_return_anything image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/58_500_error_did_not_return_anything.png)

```py
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 is the status code. 200 is ok, 201 means accepted and going to create
```

![58_add_store image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/58_add_store.png)

Now run the get all stores from the other endpoint we made

![58_stores_after_add_store image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/58_stores_after_add_store.png)

Note that this new data won't persist across runs

Now lets create items in each store
