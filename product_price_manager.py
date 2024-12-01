"""
Product Class with Price Validation

This script defines a Product class that encapsulates a product's price
and ensures the price is non-negative using property getters and setters.
It includes validation and raises an error for invalid inputs.
"""

class Product:
    """
    The Product class represents a product with a price attribute.
    It includes validation to ensure the price is non-negative.
    """

    def __init__(self, price):
        """
        Initialize a Product instance with a given price.

        Args:
            price (float): The initial price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        self.price = price  # Calls the setter for validation

    @property
    def price(self):
        """
        Getter for the price attribute.

        Returns:
            float: The current price of the product.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Setter for the price attribute with validation.

        Args:
            value (float): The new price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


def main():
    """
    Main function to demonstrate the usage of the Product class.

    Handles:
        - Creating a Product instance.
        - Accessing and updating the price attribute.
        - Handling invalid inputs with proper error messages.
    """
    try:
        # Create a Product instance
        product = Product(100)
        print(f"Initial Price: {product.price}")  # Access the price (getter)

        # Update the price (setter)
        product.price = 200
        print(f"Updated Price: {product.price}")

        # Attempt to set a negative price (raises ValueError)
        product.price = -50
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
