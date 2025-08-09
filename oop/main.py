# main.py

# This line tells Python to find your 'book_class.py' file
# and make the 'Book' class available in this script.
from book_class import Book

# This is the main function where our test code will run.
def main():
    # Create a new Book object.
    # When this line runs, it automatically calls the __init__ method in your Book class.
    my_book = Book("1984", "George Orwell", 1949)

    # Print the book object.
    # When you 'print()' an object, Python looks for its __str__ method to get a user-friendly string.
    print(my_book)

    # Get the official representation of the book object.
    # The 'repr()' function specifically calls the __repr__ method.
    print(repr(my_book))

    # Delete the reference to the book object.
    # When the last reference is gone, Python's garbage collector will eventually
    # clean up the object and call its __del__ method.
    del my_book

# This special Python construct makes sure the 'main()' function is called
# only when this script is run directly (not when it's imported as a module).
if __name__ == "__main__":
    main()