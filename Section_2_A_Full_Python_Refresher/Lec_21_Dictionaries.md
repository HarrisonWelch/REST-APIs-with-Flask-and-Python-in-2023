# Dictionaries

Another structures to interact with data. They assoc key-value pairs. Example, name and age. if you have their name you can get the age.

Keys must be hashable types, Strings are.

Index via the keys

```py
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Adam"])
```

Add one like so

```py
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Bob"] = 20

print(friend_ages)
# > {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}
```

Change one in the same way

```py
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Rolf"] = 27

print(friend_ages)
# {'Rolf': 27, 'Adam': 30, 'Anne': 27}
```

## Access twice over 

List of friends with dicts of the person's data.

```py
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

print(friends[1]["name"])
# > Adam
```

## Student attendance problem

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# > Rolf: 96
# > Bob: 90
# > Anne: 100
```

There are better ways

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# > Rolf: 96
# > Bob: 90
# > Anne: 100
```

## The `in` keyword here

The in value allowes you to check if the key is in the dictionary

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")

# > Bob: 90
```

Notice you can only check the keys.

## Grab all values

Do an average of all attendance rates.

```py
student_attendance = {"Rolf": 96, "Bob": 90, "Anne": 100}

attendance_values = student_attendance.values()

print(f"{sum(attendance_values) / len(attendance_values):.2f}")
# > 95.33
```
