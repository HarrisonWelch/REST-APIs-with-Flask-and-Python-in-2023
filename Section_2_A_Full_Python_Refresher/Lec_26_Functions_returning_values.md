# Functions returning values

```py
def add(x, y):
    print(x + y)

add(5,8)
# > 13
result = add(5,8)
# > 13
print(result)
# > None
```
By default functions return `None`

Here in the example we only print when called but don't return anything

```py
def add(x, y):
    return x + y

add(5,8)
result = add(5,8)
print(result)
# > 13
```

## And None was there

```py
def add(x, y):
    print(x+y)

print(add(5,8))
# > 13
# > None
```

Remember that return terminates the function

```py
def add(x, y):
    return
    print(x + y)
    return x + y

result = add(5,8)
print(result)
# > None
```

## Again

```py
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 3)
print(result)
# > 5.0
```

Then with zero

```py
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 0)
print(result)
# > You fool!
```

Usually not recommended to return both types number and string. Such that you can have unexpected output

```py
result = divide(15, 0) * 5
print(result)
# > You fool!You fool!You fool!You fool!You fool!
result = divide(15, 2) * 5
print(result)
# > 37.5
```