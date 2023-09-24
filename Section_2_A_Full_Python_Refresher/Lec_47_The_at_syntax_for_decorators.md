# Lec_47_The_at_syntax_for_decorators.md

Using code from previous lecture

The `@make_secure` tag will do this for us.

`@functools.wraps(func)` - keeps the name a documentation of the function passed in. Do get accusomed.

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