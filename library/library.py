class Book:
    """a book"""

    def __init__(self, title, author):  # define a method; called every time we create a new instance of the class
        self.title = title             # ...the argument `self` refers to the instance on which we are calling the method
        self.author = author

    def __str__(self):  # print this when print(classinstance)

        print_words = self.title + " by " + self.author

        return print_words



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches

    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)

        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)

        return authors

# book = Book('A Book', 'Me')

# print(book)

library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

#books = library.by_author('Carol')
print(library.titles)
print(library.authors)
