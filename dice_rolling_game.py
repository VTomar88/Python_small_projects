# This is dice rolling game
# Varsha Tomar 14 Nov 2024
# In this game if user says yes, the program will generate two numbers of a dice
# else reponse is generated if user didn't responded 'y' or 'n'
# If user input is 'n' then program exits
from random import randint

while True:
    # Ask roll the dice
    user_input = input("Roll the dice? (y/n): ").lower()
    # Check if player says no
    if user_input == 'n':
        print('Thanks for playing!')
        break # exit the loop
    # if user says yes print two random numbers
    elif user_input == 'y':
        print(f"({randint(1,6)}, {randint(1,6)})")
    else:
        # if user input other than 'y' or 'n'
        print("Invalid choice!")

