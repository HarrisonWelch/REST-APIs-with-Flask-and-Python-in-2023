# Errors in Python

```py
def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0")
        return
    return dividend / divisor


divide(15, 0)
# > Divisor cannot be 0
```

```py
def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0")
        return
    return dividend / divisor

grades = [78, 99, 85, 100]

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The average grade is {average}.")

# > Welcome to the average grade program.
# > The average grade is 90.5.

```

But what if grades is empty

```py
...
grades = []
...

# > Welcome to the average grade program.
# > Divisor cannot be 0
# > The average grade is None.
```

Could try a len check on grades. But that makes things get a bit messy.

## Raise

```py
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grades = []

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The average grade is {average}.")

# > ZeroDivisionError: Divisor cannot be 0.
```

Gives a good traceback on the error.

## Try except

```py
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grades = []

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")

# > Welcome to the average grade program.
# > Divisor cannot be 0.
# > There are no grades yet in your list.

```

There are many error types `ValueError` etc. Next lecture will be custom

You can use else in a try except. If no error happened run the else block

```py
...
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
```

## finally

This will run no matter what. if error or not.

## Multi-except

```py
...
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
except ValueError as e:
    print(e)
else:
    print(f"The average grade is {average}.")
```

This can extend to catching errors in the middle of an array processing procedure.
