# Magic methods: `__str__` and  `__repr__`

Python will call methods with double underscores on either side for you at certain points.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Person("Bob", 35)
print(bob)
# > <__main__.Person object at 0x000001E126A2E7D0>
```

This is the default behavior. print object to see info or to give a nice output.

We can define this ourselves.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

bob = Person("Bob", 35)
print(bob)
# > Person Bob, 35 years old.
```

## `__repr__` method

This used more for debugging

Note that this method will take over the `__str__` if it is unimplemented. So order or prio is `__str__`, `__repr__`, then default memory address thing.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self):
    #     return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob)
# <Person(Bob, 35)>
```

You can force a call but doing something like `bob.__repr__()`


