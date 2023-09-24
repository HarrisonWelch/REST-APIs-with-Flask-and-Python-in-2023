# Simple decorators in Python 

Wanting to secure some data.

```py
user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

print(get_admin_password())
```

Do this so we can't reach the function

```py
user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"
    
def secure_function(func):
    if user["access_level"] == "admin":
        return func

get_admin_password = secure_function(get_admin_password)

print(get_admin_password())

```

This is closer but not quite.

```py
user = {"username": "jose", "access_level": "admin"}


def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

```

So we replace the function with the original function.
