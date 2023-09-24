# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity

#     def __str__(self) -> str:
#         return f"Bookshelf with {self.quantity} books."

# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

# # shelf = BookShelf(300)
# # print(shelf)

# book = Book("Harry Potter", 120)

# print(book)

# ----


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

# shelf = BookShelf(300)
# print(shelf)


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
