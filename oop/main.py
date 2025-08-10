# main.py for Task 1

# Import all the necessary classes from library_system.py
# This line tells Python to find your 'library_system.py' file and import these classes.
from library_system import Book, EBook, PrintBook, Library

# This is the main function where our test code will run.
def main():
    # Create an instance of our Library.
    # This calls the Library class's __init__ method.
    my_library = Library()

    # Create instances of each type of book.
    # These lines call the __init__ of the respective Book, EBook, and PrintBook classes.
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500) # This is an EBook with a file_size
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234) # This is a PrintBook with a page_count

    # Add these books to the library's collection using the add_book method.
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # Ask the library to list all the books it contains.
    # This will call the list_books method in the Library class.
    my_library.list_books()

# This special Python construct makes sure the 'main()' function is called
# only when this script is run directly.
if __name__ == "__main__":
    main()