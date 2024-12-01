"""Dice Rolling Game
A program that simulates rolling a pair of dice. Each time the program runs, it
randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program display the results and ask if the
user would like to roll again.
"""
from random import randint


def dice_roll():
    """
    Simulates a dice rolling game where the user can roll two dice
    or exit the game.

    The program generates two random numbers between 1 and 6
    to simulate rolling a pair of dice. The user is prompted
    to roll the dice or exit the game in each iteration.
    """
    while True:
        # Prompt the user to roll the dice or exit
        user_input = input("Roll the dice? (y/n): ").lower()

        # Check if the user wants to exit
        if user_input == 'n':
            print('Thanks for playing!')
            break  # Exit the loop and end the game

        # Check if the user wants to roll the dice
        elif user_input == 'y':
            draws = input("How many times you wish to roll the dice: ")
            try:
                for draw in range(int(draws)):
                    # Generate and print two random numbers to simulate dice rolls
                    print(f"Draw {draw+1}: ({randint(1,6)}, {randint(1,6)})")

            except ValueError:
                print("Enter a whole number.")

        else:
            # Handle invalid inputs
            print("Invalid choice! Please enter 'y' to roll or 'n' to exit.")


if __name__ == "__main__":
    dice_roll()
