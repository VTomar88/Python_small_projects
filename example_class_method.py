"""
Book Class with Publisher Management

This script defines a Book class with instance attributes for the title and author, 
and a class attribute for the publisher. The publisher can be updated for all books 
using a class method. The script demonstrates creating book instances, updating 
the publisher, and displaying book details.
"""

class Book:
    """
    Represents a book with a title, author, and publisher.
    
    Attributes:
        publisher (str): Class attribute for the publisher, shared across all instances.
    """

    # Class attribute
    publisher = "My publisher"

    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    @classmethod
    def update_publisher(cls, new_publisher):
        """
        Update the publisher for all books.

        Args:
            new_publisher (str): The new publisher to set.
        """
        cls.publisher = new_publisher

    def get_description(self):
        """
        Get a formatted description of the book.

        Returns:
            str: A string containing the title, author, and publisher.
        """
        return f"Title: {self.title}, Author: {self.author}, Published by: {self.publisher}"


def main():
    """
    Main function to demonstrate the functionality of the Book class.

    Creates book instances, updates the publisher, and displays book details.
    """
    # Create the first book instance
    book1 = Book("Statistics 101", "Jim")
    print(book1.get_description())  # Before updating publisher

    # Update the publisher using the class method
    Book.update_publisher("Bloomsbury")

    # Create another book instance
    book2 = Book("Harry Potter", "J.K. Rowling")
    print(book2.get_description())  # After updating publisher

    # Check the first book to confirm the publisher has been updated
    print(book1.get_description())  # Should reflect the updated publisher


if __name__ == "__main__":
    main()
