# book_class.py

# This is our blueprint (class) for creating Book objects.
# This line should start at the very beginning of the file (no spaces before 'class').
class Book:
    """
    Represents a book with a title, author, and publication year.
    It demonstrates how special Python methods (magic methods) work.
    """

    # This is the constructor method. It runs automatically when you create a new Book.
    # This line should be indented exactly 4 spaces from the 'class Book:' line.
    def __init__(self, title, author, year):
        """
        Initializes a new Book instance with its title, author, and publication year.
        The 'self' keyword refers to the specific Book object being created.
        """
        # These lines should be indented exactly 8 spaces from the 'class Book:' line.
        self.title = title   # Assigns the given title to this book object
        self.author = author # Assigns the given author to this book object
        self.year = year     # Assigns the given year to this book object
        print(f"Book '{self.title}' created.") # A message to confirm creation (helpful for debugging)

    # This is the destructor method. It runs automatically when a Book object is deleted.
    # This line should be indented exactly 4 spaces from the 'class Book:' line.
    def __del__(self):
        """
        Called when a Book object is about to be completely removed from memory.
        It's used for any final cleanup.
        """
        # This line should be indented exactly 8 spaces from the 'class Book:' line.
        print(f"Deleting {self.title}") # Prints a message when the book is deleted

    # This is the string representation for users. Used by 'print()'.
    # This line should be indented exactly 4 spaces from the 'class Book:' line.
    def __str__(self):
        """
        Returns a friendly, easy-to-read string description of the book.
        This is what you see when you use 'print(my_book)'.
        """
        # This line should be indented exactly 8 spaces from the 'class Book:' line.
        return f"{self.title} by {self.author}, published in {self.year}"

    # This is the official string representation for developers. Used by 'repr()'.
    # This line should be indented exactly 4 spaces from the 'class Book:' line.
    def __repr__(self):
        """
        Returns a developer-focused string that could potentially recreate the object.
        This is what you see when you use 'repr(my_book)' or in the interactive Python interpreter.
        """
        # This line should be indented exactly 8 spaces from the 'class Book:' line.
        return f"Book('{self.title}', '{self.author}', {self.year})"