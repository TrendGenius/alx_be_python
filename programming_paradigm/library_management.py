#!/usr/bin/env python3
"""
This module implements a basic library management system using OOP principles.
It includes classes for Book and Library.
"""

class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        # Private attribute to track the book's checkout status.
        self._is_checked_out = False

    def check_out(self):
        """
        Changes the book's status to checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Changes the book's status to available.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a Library object with an empty list of books.
        """
        # Private list to store Book objects.
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book instance to add.
        """
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Finds a book by title and checks it out if available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book.check_out()
                    print(f"Checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"Error: Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Finds a book by title and marks it as returned.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book.return_book()
                    print(f"Returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"Error: Book '{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints a list of all books that are currently available.
        """
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
