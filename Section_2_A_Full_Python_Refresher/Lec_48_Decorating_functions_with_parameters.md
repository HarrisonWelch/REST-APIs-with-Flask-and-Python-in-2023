# Decorating functions with parameters

From prev lecture

```py
import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


# get_admin_password = make_secure(get_admin_password)

print(get_admin_password.__name__)

```

Which then moves to this

```py
import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


# get_admin_password = make_secure(get_admin_password)

print(get_admin_password.__name__)


```

`*args, **kwargs` so we can cater to everything
