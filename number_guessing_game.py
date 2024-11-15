# This is number guessing game. User has to guess a number between 1 and 100. 
# If user guesses some other number or something else, program will ask to enter a valid nunber. 
# Then computer has to pick a random number. If user number guessed is greater than the picked number print too high
# If user guessed number is low, print 'too low'
# Once user reaches the end of the game, say congratulations and tell how many user took tries to reach the guessed number.

from random import randint

# computer guess
comp_guess = randint(1,100)
# initialize count
count = 0
# while true loop
while True:
    try:
        # user input and turn it into integer
        user_input = int(input('Guess the number between 1 and 100: '))
        # if user input is between 1 and 100
        if user_input >= 1 and user_input <= 100:
            # if user input greater than computer guess
            if user_input > comp_guess:
                print("Too High!")
            # if user input less than computer guess
            if user_input < comp_guess:
                print("Too Low!")
            # if user input equals computer guess
            if user_input == comp_guess:
                print(f"Congratulations! You guessed the number in {count+1} try!")
                break
        # else ask to enter a valid number
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a integer between 1 and 100")
    # run the couter
    count += 1
