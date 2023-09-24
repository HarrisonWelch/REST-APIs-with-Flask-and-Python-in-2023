# First-class functions

Functions are treated as variables.

```py
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator): # Looks wierd
    return operator(*values)

result = calculate(20, 4, operator=divide)

print(result)
```

We pass the `divide` function as the operator. Notice no parenthesis so we are passing it as a var not calling it.

## Another example

```py
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Bob Smith", get_friend_name))

# > RuntimeError: Could not find element with Bob Smith
```

But now we fix it to find a name that exists.

```py
...
print(search(friends, "Rolf Smith", get_friend_name))
# > {'name': 'Rolf Smith', 'age': 24}
```

With lambdas

```py
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# > {'name': 'Rolf Smith', 'age': 24}
```

With `itemgetter`

```py
print(search(friends, "Rolf Smith", itemgetter("name")))
# > {'name': 'Rolf Smith', 'age': 24}
```
