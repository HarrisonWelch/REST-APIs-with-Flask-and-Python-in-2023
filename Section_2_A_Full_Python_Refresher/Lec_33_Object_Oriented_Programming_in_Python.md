# Object Oriented Programming in Python

OOP allows us to think about things we see in the real world as code.

```py
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))
# > 88.0
```

We want to be able to use that on the student "object" like so:

```py
print(student.average())
```

`self` is the convention

```py
class Student:
    def __init__(self):
        self.name = "Rolf"

student = Student()
print(student.name)
# > Rolf
```

The grades can be added

```py

class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

student = Student()
print(student.name)
# > Rolf
print(student.grades)
# > (90, 90, 93, 78, 90)

```

## Class methods

init class method runs on instantiate.

```py
class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()

print(Student.average(student))
# > 88.2
```

You can also just call it on the object

```python
...
print(student.average())
# > 88.2
```

All methods in the class need a param called `self` but can include more

```py
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
print(student.name)
# > Bob
print(student.average_grade())
# > 92.2
```

Can reuse to make more students

```py
student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))
print(student.average_grade())
# > 92.2
print(student2.average_grade())
# > 88.2
```
