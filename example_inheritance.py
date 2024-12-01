class InvalidOperatorError(Exception):
    """
    Custom exception raised for invalid operations on a stream.

    Examples of invalid operations:
    - Opening an already opened stream.
    - Closing an already closed stream.
    """
    pass


class Stream:
    """
    A base class for managing the state of a generic stream.

    Attributes:
        open (bool): Tracks whether the stream is open (True) or closed (False).
    """

    def __init__(self):
        """
        Initialize a Stream instance with the stream in a closed state.
        """
        self.open = False

    def opened(self):
        """
        Open the stream. If the stream is already open, raise an InvalidOperatorError.

        Raises:
            InvalidOperatorError: If the stream is already open.
        """
        if self.open:
            raise InvalidOperatorError("Already opened")
        self.open = True

    def closed(self):
        """
        Close the stream. If the stream is already closed, raise an InvalidOperatorError.

        Raises:
            InvalidOperatorError: If the stream is already closed.
        """
        if not self.open:
            raise InvalidOperatorError("Already closed")
        self.open = False


class FileStream(Stream):
    """
    A subclass of Stream representing a file-based stream.

    Methods:
        read(): Reads data from a file.
    """

    def read(self):
        """
        Simulate reading data from a file.
        """
        print("Reading data from a file")


class NetworkStream(Stream):
    """
    A subclass of Stream representing a network-based stream.

    Methods:
        read(): Reads data from a network.
    """

    def read(self):
        """
        Simulate reading data from a network.
        """
        print("Reading data from a network")


# Usage
# Using FileStream
def main():
    """
    Main function to demonstrate the usage of Class inheritance
    """
    try:
        file_stream = FileStream()
        file_stream.opened()  # Open the stream
        file_stream.read()    # Read from the file
        file_stream.closed()  # Close the stream

        # Attempting to close an already closed stream
        file_stream.closed()
    except InvalidOperatorError as e:
        print(f"Error: {e}")

    print("\n")

    # Using NetworkStream
    try:
        network_stream = NetworkStream()
        network_stream.opened()  # Open the stream
        network_stream.read()    # Read from the network
        network_stream.closed()  # Close the stream

        # Attempting to open an already open stream
        network_stream.opened()
    except InvalidOperatorError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
