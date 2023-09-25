# Lec_55_Your_first_REST_API_endpoint.md

Picking up from last lecture

```py
from flask import Flask

app = Flask(__name__)  # Creates flask app that does a lot for us
```

Going to put the data in a python list, DB later.

```py
from flask import Flask

app = Flask(__name__)  # Creates flask app that does a lot for us

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") # Endpoint. http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

```

Returns:

![55_store_return image](https://github.com/HarrisonWelch/REST-APIs-with-Flask-and-Python-in-2023-Notes/blob/master/Screenshots/55_store_return.png)

Spaces and tabs don't matter in JSON. Order does not matter in JSON. 

We'll talk about what JSON is in the next lecture.

