# Lec_56_What_is_JSON

https://rest-apis-flask.teclado.com/docs/first_rest_api/what_is_json/

JSON is a long string of data. contents follow a specific format

```json
{
    "key": "value"
}
```

At core:
* Strings
* Numbers
* Booleans
* Lists
* Objects (like python dictionary)

Flask turns it into JSON for us. JSON needs a stringify.

Python keywords will transform to JSON keywords `True` -> `true`

Non-pretty is smaller and less data. Prettify is done on the received client.
