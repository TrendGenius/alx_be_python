# library_system.py

# --- Base Class: Book ---
# This is the most general type of book. All other specific book types will be based on this.
class Book:
    """
    Base class for all books. Contains attributes common to all book types.
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

# --- Derived Class (Inheritance): EBook ---
# EBook is a 'Book' but with an extra attribute: file_size.
# The '(Book)' means EBook inherits from the Book class.
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
        # Call the constructor of the parent class (Book).
        # This ensures 'title' and 'author' are set up by the Book's __init__ method.
        super().__init__(title, author)
        self.file_size = file_size # EBook's unique attribute

# --- Derived Class (Inheritance): PrintBook ---
# PrintBook is also a 'Book' but with an extra attribute: page_count.
# The '(Book)' means PrintBook also inherits from the Book class.
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
# A Library is not a type of Book; instead, it *contains* (is composed of) Books.
class Library:
    """
    Represents a library that manages a collection of various book types.
    Demonstrates composition (a Library 'has-a' list of books).
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self.books = [] # This list will hold instances of Book, EBook, and PrintBook

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
        It uses 'isinstance' to check the specific type of book and print relevant details.
        """
        print("\n--- Books in the Library ---")
        if not self.books: # Check if the library is empty
            print("The library is currently empty.")
            return

        for book in self.books:
            # Check the actual type of the 'book' object to print its specific details
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book): # This catches any general Book objects (or acts as a fallback)
                print(f"Book: {book.title} by {book.author}")
            else:
                print(f"Unknown item in library: {book}") # For any unexpected object type