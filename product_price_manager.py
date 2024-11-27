class Product:
    """The Product class encapsulates a product's price with validation to ensure it is non-negative.
    """

    def __init__(self, price):
        self.price = price  # Calls the setter for validation

    @property
    def price(self):
        """Getter for price."""
        return self.__price

    @price.setter
    def price(self, value):
        """Setter for price with validation."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


# Creating a Product instance
try:
    product = Product(100)
    print(f"Initial Price: {product.price}")  # Access the price (getter)

    # Update the price (setter)
    product.price = 200
    print(f"Updated Price: {product.price}")

    # Attempt to set a negative price (raises ValueError)
    product.price = -50
except ValueError as e:
    print(e)
