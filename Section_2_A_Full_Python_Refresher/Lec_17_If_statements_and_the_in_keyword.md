# If statements and the in keyword

```py
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    # Remember indentation
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")
```

Output

```
Enter something you've watched recently: Green Book
I've watched Green Book too!
...
Enter something you've watched recently: Monty Python
I haven't watched that yet.
```

## Magic number app

```py
number = 7

user_input = input("Enter 'y' if you would like to play: ")

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        # Two sets of indentation now for the nested if
        print("You guess correctly!")
    else:
        print("Sorry, it's wrong!")
```

Output

```
Enter 'y' if you would like to play: y
Guess our number: 7
You guess correctly!
...
Enter 'y' if you would like to play: y
Guess our number: 5
Sorry, it's wrong!
```

What if they put in an uppercase Y

first instinct to put in the `lower()` after input.

Could also put the in keyword in the if statement to make it exe regard less of case

```py
if user_input in ("Y", "y"):
    ...
```

Or we could use the `in` keyword where we tell the user if we were off by one.

```py
number = 7

user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("Y", "y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        # Two sets of indentation now for the nested if
        print("You guess correctly!")
    elif number - user_number in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

```
Output

```
Enter 'y' if you would like to play: y
Guess our number: 6
You were off by one.
```

But it would be much easier to throw in the `abs()` function for the absolute value of the difference which is always in positive terms.

```py
number = 7

user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("Y", "y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        # Two sets of indentation now for the nested if
        print("You guess correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
```

Output
```
Enter 'y' if you would like to play: y
Guess our number: 6
You were off by one.
...
Enter 'y' if you would like to play: y
Guess our number: 8
You were off by one.
```
