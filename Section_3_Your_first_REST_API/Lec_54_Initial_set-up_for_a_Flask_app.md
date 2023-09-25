# Initial set-up for a Flask app

python -m venv .venv

In terminal run <path-to-venv>/Scripts/activate.bat

Then your terminal will have `(.venv)` in front to signify its working

```
(.venv) C:\...\REST_APIs_with_Flask_and_Python_in_2023\Section_3_Your_first_REST_API\.venv\Scripts>
```

Then run `pip install flask` in the virtual env. Lib/site-packages should have stuff in it.

```py
from flask import Flask

app = Flask(__name__) # Creates flask app that does a lot for us
```

Filname and variable must be app.

Now run with `flask run`

```sh
>flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Running IP is in the logs above. We will be able to intercept that data and do something with it.

`Ctrl+c` to stop

Now we are ready to make an endpoint.
