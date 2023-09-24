# Class composition

Classes that use other classes

Allowes classes to be simpler and more manageable

```py
class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __str__(self) -> str:
        return f"Bookshelf with {self.quantity} books."

shelf = BookShelf(300)

print(shelf)

# > Bookshelf with 300 books.
```

Book example. You should not inherit from the bookshelf because a book does not have a quantity.

This looks awkward

```py
# THIS IS BAD DONT DO THIS
class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __str__(self) -> str:
        return f"Bookshelf with {self.quantity} books."

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

# shelf = BookShelf(300)
# print(shelf)

book = Book("Harry Potter", 120)

print(book)

# > Book Harry Potter
```

* Why inherit when we aren't going to use the shelf?
* A book is not a bookshelf

## Composition

```py
class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
# > Bookshelf with 2 books.
```
