# List comprehensions in Python

Say we have a list of numbers and we want to get another list of all the same numbers doubled.

Traditional

```py
numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num*2)

print(doubled)
# > [2, 6, 10]
```

put the line then the loop with list comp

```py
numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)
# > [2, 6, 10]
```

## Start with 'S' problem

We have a list of names and want to get a list of names that start with "S"

Traditional way

```py
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = []

for friend in friends:
    if friend.startswith("S"):
        start_s.append(friend)

print(start_s)
# > ['Sam', 'Samantha', 'Saurabh']
```

ListComp way

```py
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)
```

Note that these are two different lists event if they have the same values. Remove the non-S names to demonstrate.

```py
friends = ["Sam", "Samantha", "Saurabh"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)
# > ['Sam', 'Samantha', 'Saurabh']
print(friends == start_s)
# > True
print(friends is start_s)
# > False
print("friends:", id(friends), "starts_s:", id(start_s))
# > friends: 1659413418560 starts_s: 1659414869376
```

The id is a relative to cpython memory address.
