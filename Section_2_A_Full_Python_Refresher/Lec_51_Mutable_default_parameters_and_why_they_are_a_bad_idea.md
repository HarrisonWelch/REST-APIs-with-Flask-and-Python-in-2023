# Mutable default parameters and why they are a bad idea

Need to know about in Python to save the headache

```py
from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []): # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)

# > [90]
```

What if we add a new student Rolf.

```py
from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

```

Out

```
[90]
[90]
```

This is bad. Rolf did not take any exams but has a score of 90 somehow.

The default params are resolved on function loading.

Instead make the default array `= None` and/or have the `self.grades = grades or []`

Or you can do an Optional

```py
from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # This is bad!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

```

Output

```
[90]
[]
```
