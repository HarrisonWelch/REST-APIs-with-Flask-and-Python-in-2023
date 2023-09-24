# Unpacking keyword arguments

Last video was confusing, this video will be more confusing.

kwargs is a convention not a rule.

```py
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)
# > {'name': 'Bob', 'age': 25}
```

`**` will collect keyword arguments.

## Reverse it

```py
def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)
# > Bob 25
```

## You can do both pack and unpack

```py
def named(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 25}

named(**details)
# > {'name': 'Bob', 'age': 25}
```

## More complex

```py
def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

# > {'name': 'Bob', 'age': 25}
# > name: Bob
# > age: 25
```

## Both

```py
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)

# > (1, 3, 5)
# > {'name': 'Bob', 'age': 25}
```

Normally used so some of all of those args can be passed on to another function

Example:
```python
"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""
```

Same thing but adds another argument. Pass from one thing to another until used - common thing.

```py
def my_function(**kwargs):
    print(kwargs)

my_function(**"Bob")
# > TypeError: __main__.my_function() argument after ** must be a mapping, not str
my_function(**None)
# > TypeError: __main__.my_function() argument after ** must be a mapping, not NoneType
```
