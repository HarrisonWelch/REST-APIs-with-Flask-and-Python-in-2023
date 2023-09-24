# Unpacking arguments

```py
def multiply(*args):
    print(args)

multiply(1, 3, 5)
# > (1, 3, 5)
```

`*args` will collect.

Can also operate over that collected tuple

```py
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))
# > (1, 3, 5)
# > 15
```

Passing 1 arg will do the same but make a tuple of a single arg

Can use the asterisk to destruct into args

```py
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))
# > 8
```

The number of elements in the array must match else error

You can also do this

```py
def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))
# > 40
```

But there is a smarter way with `**`

```py
nums = {"x": 15, "y": 25}
print(add(**nums))
# > 40
```

Python will grab the keys as the named args.
