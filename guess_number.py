"""
Guess the Number Game

This script implements a simple number guessing game where the user has three attempts
to guess a secret number. If the user guesses correctly, they win; otherwise, they lose.
"""

def guess_number_game(secret_num, max_attempts=3):
    """
    Runs the Guess the Number game.

    Args:
        secret_num (int): The secret number to guess.
        max_attempts (int): Maximum number of attempts allowed (default is 3).

    Returns:
        None
    """
    attempts = 0

    while attempts < max_attempts:
        try:
            # Prompt the user to make a guess
            guess = int(input('Guess the number: '))

            # Check if the guess is correct
            if guess == secret_num:
                print('You win!')
                break
            else:
                print('Wrong guess, try again.')
            
            # Increment the attempts counter
            attempts += 1

        except ValueError:
            # Handle invalid input
            print("Invalid input! Please enter a number.")

    else:
        # If the user fails to guess within the allowed attempts
        print('You fail! The secret number was:', secret_num)


def main():
    """
    Main function to start the game.

    Returns:
        None
    """
    print("Welcome to the Guess the Number Game!")
    secret_number = 10  # Define the secret number
    guess_number_game(secret_number)


if __name__ == "__main__":
    main()
