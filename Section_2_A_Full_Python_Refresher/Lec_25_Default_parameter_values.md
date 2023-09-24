# Default parameter values

Starting

```python
def add(x, y):
    print(x + y)

add(5, 8)
# 13
```

Now you can define the function as `def add(x, y=8):`

Now if y is not provided it will be 8

```python
def add(x, y-8):
    print(x + y)

add(5)
# 13
```

What you cant do is `y=5`

```python
def add(x, y-8):
    print(x + y)

add(y=5)
# > TypeError: add() missing 1 required positional argument: 'x'
```

Just like with named arguments you cant follow a default with a non-default arg

```py
def add(x=5, y):
    print(x + y)

add(5, 8)
# > SyntaxError: non-default argument follows default argument
```

## Dont make default args from variables

```py

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)

default_y = 4

add(2)
```

Output

```
5
5
```

This can be very confusing
