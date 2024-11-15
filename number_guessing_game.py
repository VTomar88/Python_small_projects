# This is number guessing game. User has to guess a number between 1 and 100. 
# If user guesses some other number or something else, program will ask to enter a valid nunber. 
# Then computer has to pick a random number. If user number guessed is greater than the picked number print too high
# If user guessed number is low, print 'too low'
# Once user reaches the end of the game, say congratulations and tell how many user took tries to reach the guessed number.

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
            if 1<= user_input <= 100:
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
