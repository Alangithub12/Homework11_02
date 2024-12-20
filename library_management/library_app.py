# library_app.py

import json
import logging

# Настройка логирования
logging.basicConfig(filename='library.log', level=logging.INFO)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Librarian:
    def add_book(self, library, book):
        library.add_book(book)
        logging.info(f"Книга добавлена: {book}")

    def remove_book(self, library, book):
        library.remove_book(book)
        logging.info(f"Книга удалена: {book}")


class Reader:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        return self.books

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)
            logging.info("Книги сохранены в файл.")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            books_data = json.load(f)
            self.books = [Book(**data) for data in books_data]
            logging.info("Книги загружены из файла.")


# Пример использования
if __name__ == "__main__":
    library = Library()
    librarian = Librarian()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    librarian.add_book(library, book1)
    librarian.add_book(library, book2)

    print("Книги в библиотеке:")
    for book in library.list_books():
        print(book)

    librarian.remove_book(library, book1)

    print("Книги после удаления:")
    for book in library.list_books():
        print(book)

    library.save_to_file("library.json")
    library.load_from_file("library.json")