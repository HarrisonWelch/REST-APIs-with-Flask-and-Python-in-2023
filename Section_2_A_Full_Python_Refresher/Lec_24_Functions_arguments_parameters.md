# Functions arguments parameters

parameters x and y created for the function. at the end of the function they disappear

```py
def add(x, y): # Params x and y
    result = x + y
    print(result)

add(5, 3)
```

Output
```
8
```

## Give too many args

```py
def say_hello():
    print("Hello")

say_hello("Bob")
# > TypeError: say_hello() takes 0 positional arguments but 1 was given
```

## Positional arguments

Python will assign the position of the argument to the parameter. 

```py
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Bob", "Smith")
# > Hello, Bob Smith
```

There are also named args

## Named args, Keyword args

```py
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Bob", name="Smith")
# > Hello, Smith Bob
```

Now Python will assign not on postion but the label we gave it.

If you want to mix and match position and keyword args, the keyword args must come later

```py
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(15, divisor=0)
# > You fool!
divide(dividend=15, 0)
# > SyntaxError: positional argument follows keyword argument
```
