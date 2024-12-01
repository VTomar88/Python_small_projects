"""
Car Game

A simple text-based car game focusing on loop control and if-else statements.
The game provides basic commands to start, stop, and quit the car while handling
user input validation and state management.
"""


def display_help():
    """
    Displays the available commands to the user.
    """
    print("""
start - to start the car
stop - to stop the car
quit - to exit
""")


def handle_start(started):
    """
    Handles the 'start' command for the car.

    Args:
        started (bool): Current state of the car (True if started, False otherwise).

    Returns:
        bool: Updated state of the car.
    """
    if started:
        print('Car already started.')
    else:
        print('Car started...Ready to go!')
        started = True
    return started


def handle_stop(started):
    """
    Handles the 'stop' command for the car.

    Args:
        started (bool): Current state of the car (True if started, False otherwise).

    Returns:
        bool: Updated state of the car.
    """
    if not started:
        print('Car is already stopped.')
    else:
        print('Car stopped.')
        started = False
    return started


def car_game():
    """
    Main function to handle the car game loop.
    Accepts user input and processes commands to start, stop, or quit the game.
    """
    started = False
    while True:
        user_input = input('> ').lower()

        # Handle commands
        if user_input == 'help':
            display_help()
        elif user_input == 'start':
            started = handle_start(started)
        elif user_input == 'stop':
            started = handle_stop(started)
        elif user_input == 'quit':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("I don't understand that...")


if __name__ == "__main__":
    car_game()
