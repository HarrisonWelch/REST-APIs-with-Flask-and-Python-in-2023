## If statements

Ask use if it is monday

```py
day_of_week = input("What day of the week is it today? ")

print(day_of_week == "Monday")
```

Output

```
What day of the week is it today? Monday
True
```

Swap into an if statement

```python
day_of_week = input("What day of the week is it today? ")

# print(day_of_week == "Monday")

if day_of_week == "Monday":
    # There a few spaces here for indentation
    # That is how python tells what code is in here.
    print("Have a great start to your week!")
```

Recommend using 4 spaces for python code

Code ouside of the if statement will always run

Example:

```py
day_of_week = input("What day of the week is it today? ")

# print(day_of_week == "Monday")

if day_of_week == "Monday":
    # There a few spaces here for indentation
    # That is how python tells what code is in here.
    print("Have a great start to your week!")

print("This will always run")
```

The line `print("This will always run")` will always execute.

## Not equal

```py
day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")

if day_of_week != "Monday":
    print("Full speed ahead!")

print("This will always run")

```

Output

```
What day of the week is it today? Monday
Have a great start to your week!
This will always run

...
What day of the week is it today? Tuesday
Full speed ahead!
This will always run
```

Just do `else`

```py
day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
else:
    print("Full speed ahead!")

print("This will always run")
```

Then elif to avoid non-needed checks

```py
day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Tuesday":
    print("It's Tuesday.")
else:
    print("Full speed ahead!")

print("This will always run")
```

Now if the first is true there is no need to check the 2nd block there.

Order is important. `elif` and `else` must come after `if`.

## User input incongruence

What if they say "monday" instead of "Monday". They won't go into the if statement for monday.

Output

```
What day of the week is it today? monday
Full speed ahead!
This will always run
```

Recommendation is to put `.lower()` after input is accepted.

Then flip the if statements to lowercase as well.

```py
day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday.")
else:
    print("Full speed ahead!")

print("This will always run")
```

Output

```
What day of the week is it today? monday
Have a great start to your week!
This will always run
```
