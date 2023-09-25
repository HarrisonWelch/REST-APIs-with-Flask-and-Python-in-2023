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


@app.get("/store")  # Endpoint. http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}
