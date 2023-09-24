# Loops in Python

Allows repeat code a number of times.

Start with code from last video

Common convention of "Y/n"

change the if statement to a while loop.

```py
number = 7

user_input = input("Would you like to play? (Y/n) ")

while user_input !=  "n":
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
Would you like to play? (Y/n) y
Guess our number: 1
Sorry, it's wrong!
Guess our number: 2
Sorry, it's wrong!
Guess our number: 3
Sorry, it's wrong!
Guess our number: 4
Sorry, it's wrong!
Guess our number: 5
Sorry, it's wrong!
Guess our number: 6
You were off by one.
Guess our number: 7
You guess correctly!
Guess our number: 8
You were off by one.
Guess our number: 9
Sorry, it's wrong!
Guess our number: 10
Sorry, it's wrong!
```

But we need to allow the user to leave the loop so we reask the "like to play"

Problem is that we have to update the prompt twice if we want to change it.

So we move the original ask inside the loop. Change the while to always be true. Then if we say no break out of the loop.

```py
number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

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
Would you like to play? (Y/n) y
Guess our number: 10
Sorry, it's wrong!
Would you like to play? (Y/n) n
```

## For loop

```py
friends = ["Rolf", "Jen", "Bob", "Anne"]

print(f"{friends[0]} is my friend.")
print(f"{friends[1]} is my friend.")
print(f"{friends[2]} is my friend.")
print(f"{friends[3]} is my friend.")
```

This is very cumbersome. So we use a for loopp

```py
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")
```

`friend` will become the 1st value, next iteration take the next friend.

Output

```
Rolf is my friend.
Jen is my friend.
Bob is my friend.
Anne is my friend.
```

Can also do a `range` for the loop source to exe a number of times.

```py
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in range(4):
    print(f"{friend} is my friend.")
# > 0 is my friend.
# > 1 is my friend.
# > 2 is my friend.
# > 3 is my friend.
```

## Grades problem

```py
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)
# > 80.0
```

But here we can use `sum()`

Remeber to search for everything so you're always absorbing info and learning new solution.

```py
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)
# > 80.0
```
