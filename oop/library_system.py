# library_system.py
# This file defines the classes for the library system: Book, EBook, PrintBook, and Library.
# --- Base Class: Book ---
# This is the foundational class for any book, holding common attributes.
class Book:
    """
    Base class for all books in the library system.
    Contains attributes common to all book types like title and author.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        This is what gets printed when you use `print(book_object)`.
        """
        return f"{self.title} by {self.author}"

# --- Derived Class (Inheritance): EBook ---
# EBook inherits from Book, adding specific attributes for electronic books.
class EBook(Book):
    """
    Represents an electronic book, inheriting from the base Book class.
    Adds a specific attribute for file size.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        # Call the constructor of the parent class (Book) using super().
        # This properly initializes the 'title' and 'author' attributes.
        super().__init__(title, author)
        self.file_size = file_size # EBook's unique attribute

# --- Derived Class (Inheritance): PrintBook ---
# PrintBook also inherits from Book, adding attributes unique to physical books.
class PrintBook(Book):
    """
    Represents a physical print book, inheriting from the base Book class.
    Adds a specific attribute for page count.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the constructor of the parent class (Book).
        super().__init__(title, author)
        self.page_count = page_count # PrintBook's unique attribute

# --- Composition Class: Library ---
# The Library class 'has' (is composed of) different types of book objects.
class Library:
    """
    Represents a library that manages a collection of various book types.
    Demonstrates composition by containing book objects within a list.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self.books = [] # This list stores instances of Book, EBook, and PrintBook

    def add_book(self, book):
        """
        Adds any type of book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints details of each book currently in the library.
        It uses 'isinstance' to identify the specific type of book for detailed output.
        """
        print("\n--- Books in the Library ---")
        if not self.books: # Check if the library is empty
            print("The library is currently empty.")
            return

        for book in self.books:
            # Check the actual type of the 'book' object using isinstance()
            # Now, we can also leverage the __str__ method of the Book (or its child classes)
            if isinstance(book, EBook):
                # For EBook, we combine its __str__ output (from Book) with its unique attribute
                print(f"{book.__str__()}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                # For PrintBook, same thing, combine its __str__ with its unique attribute
                print(f"{book.__str__()}, Page Count: {book.page_count}")
            elif isinstance(book, Book): # Catches general Book objects
                print(f"Book: {book.__str__()}") # Explicitly use Book's __str__
            else:
                print(f"Unknown item in library: {book}") # For unexpected object types
