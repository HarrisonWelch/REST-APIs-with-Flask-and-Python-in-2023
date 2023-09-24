# Coding Exercise 3 Flow control-loops and ifs

1. Change loop so that only even numbers go into variable `evens`
2. Add clause to the if block so that if "q" is input, "Quit" is printed

## Answer

```py
# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")
```
