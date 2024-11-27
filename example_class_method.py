class Book:
    # Class attribute
    publisher = "My publisher"

    def __init__(self, title, author):
        # Instance attributes
        self.title = title
        self.author = author

    @classmethod
    def update_publisher(cls, new_publisher):
        """Update the publisher for all books."""
        cls.publisher = new_publisher

    def get_description(self):
        """Return a formatted description of the book."""
        return f"Title: {self.title}, Author: {self.author}, Published by: {self.publisher}"


# Create a book instance and print its description
book1 = Book("Statistics 101", "Jim")
print(book1.get_description())  # Before updating publisher

# Update the publisher using the class method
Book.update_publisher("Bloomsbury")

# Create another book instance and print its description
book2 = Book("Harry Potter", "J.K. Rowling")
print(book2.get_description())  # After updating publisher

# Check book1 again to ensure the publisher has been updated
print(book1.get_description())  # Should reflect the updated publisher
