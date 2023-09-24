# Type hinting in Python 3.5+

Just to help you the dev

```py
def list_avg(sequence):
    return sum(sequence) / len(sequence)

list_avg(123)
# > TypeError: 'int' object is not iterable
```

Nothing there to tell you that you may be making a mistake

```py
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)
```

VScode won't tell you that you aren't make a mistake. PyCharm or some VScode packages (linters) will tell you that you may be making a mistake.

There is a more common way of typing hinting via imports.

```py
from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)
```

Still will error out tho.

## Book example

```py
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
```

## Bookshelf

This is how you type hint a List of objects

```py
from typing import List # Tuple, Set etc...


class Book:
    pass


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."
```

## Book example from static methods lecture

* `-> str` to hint a string is returned
* `-> "Book"` to hint that Book object is returned. Note the quote marks
* If it happens to return a diff class you don't need the quotes ie `-> Bookshelf`

```py
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: str):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[1], page_weight)
```


