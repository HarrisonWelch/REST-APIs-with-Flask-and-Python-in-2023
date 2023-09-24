# @classmethod and @staticmethod

```py
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
```

Output

```
Called instance_method of <__main__.ClassTest object at 0x000001D4D6E5EAD0>
Called instance_method of <__main__.ClassTest object at 0x000001D4D6E5EAD0>
```

instance = object

## @classmethod

Uses the class for something

```py
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

ClassTest.class_method() # Python smart enough to pass in ClassTest as the 1st arg

```

Output

```
Called class_method of <class '__main__.ClassTest'>
```

## @staticmethod

Function in a class. Does not use self

```py
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

ClassTest.static_method()

# > Called static_method.
```

instance method used for most things. Class methods used often for `factories`. Static methods are used for code organization.

## Using class method

```py
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"


book = Book("Harry Potter", "hardcover", 1500)

print(book)
# > <Book Harry Potter, hardcover, weighing 1500g>
```

Now introduce the class method.

```py
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

# book = Book("Harry Potter", "hardcover", 1500)
book = Book.hardcover("Harry Potter", 1500)

print(book)
# > <Book Harry Potter, hardcover, weighing 1600g>
```

You can also introduce the paperback classmethod

```py
class Book:

    ...
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)
...
light = Book.paperback("Python 101", 1500)

...
print(light)
# > <Book Python 101, paperback, weighing 1500g>
```

"cls" is the book class. Use that instead of book

```py
...
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight)
...
```
