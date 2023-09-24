# Destructuring

Something we looked at in the for loop on a dict. But now lets look harder.

`x = 5, 11` - this will result in a tuple of the two values.

You can destruct like so

```py
x, y = 5, 11
print(x, y)
# > 5 11
```

Back to the prev example

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

print(list(student_attendance.items()))

# > [('Rolf', 96), ('Bob', 90), ('Anne', 100)]
```

Means that we get 3 diff tuples and destruct over them each loop iteration.

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

for t in student_attendance.items():
    print(t)

# > ('Rolf', 96)
# > ('Bob', 90)
# > ('Anne', 100)
```

Quite prevalent in python

## Name age profession

List of people with name age profession

```python
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# > Name: Bob, Age: 42, Profession: Mechanic
# > Name: James, Age: 24, Profession: Artist
# > Name: Harry, Age: 32, Profession: Lecturer
```

If any value is missing in the tuples

```py
people = [("Bob", 42), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# > ValueError: not enough values to unpack (expected 3, got 2)
```

You can also index them like so instead of destructing

```python
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# > Name: Bob, Age: 42, Profession: Mechanic
# > Name: James, Age: 24, Profession: Artist
# > Name: Harry, Age: 32, Profession: Lecturer
```

This is much less readable tho, not sure what is going on.

## Underscores

Use an underscore by itself to destruct and ignore one of the values.

```python
person = ("Bob", 42, "Mechanic")

name, _, profession = person

print(name, profession)
# > Bob Mechanic
```

Here the age will be ignored

## Head, and tail (Collecting)

The first arg will get the first element in the list and the 2nd arg will collect all remaining elements.

```python
head, *tail = [1, 2, 3, 4, 5]

print(head)
# > 1
print(tail)
# > [2, 3, 4, 5]
```

It can be reversed too

```python
*head, tail = [1, 2, 3, 4, 5]

print(head)
# > [1, 2, 3, 4]
print(tail)
# > 5
```

You can use asterisks elsewhere too like in the print statement

```py
print(* head)
# > 1 2 3 4
```

The brackets fall away. Going to talk later about this
