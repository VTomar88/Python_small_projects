"""Number Guessing Game
A program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.
"""

from random import randint


def get_computer_guesses():
    """Generates a random number from 1 to 100"""
    return randint(1, 100)


def get_user_input():
    """Prompts the user to guess a number between 1 and 100 and validates the input."""
    while True:
        try:
            # user input and turn it into integer
            user_input = int(input('Guess the number between 1 and 100: '))
            # if user input is between 1 and 100
            if 1 <= user_input <= 100:
                return user_input
            else:
                print("Enter a valid number!")
        except ValueError:
            print("Enter an integer!")


def check_guess(user_input, comp_guess):
    """Compares the user's guess to the computer's number and returns the comparison result."""
    if user_input > comp_guess:
        return "Too High!"
    # if user input less than computer guess
    if user_input < comp_guess:
        return "Too Low!"
    # if user input equals computer guess
    if user_input == comp_guess:
        return "correct"


def play_game():
    """Play the game"""
    comp_guess = get_computer_guesses()
    # initialize count
    count = 0
    # while true loop
    while True:
        # get user input and validate it
        user_input = get_user_input()
        result = check_guess(user_input, comp_guess)
        # Run the counter
        count += 1

        # Check the result
        if result == 'correct':
            print(f"Congratulations! You guessed the number in {count} try!")
            break
        else:
            print(result)


if __name__ == "__main__":
    play_game()
