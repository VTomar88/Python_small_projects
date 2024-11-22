# Guess the number in three guess if guessed then user win else failed

secret_num = 10
count_guess = 0
while count_guess < 3:
    guess = int(input('Guess: '))
    # Find if the guess is same as secret number
    if guess == secret_num:
        print('You win!')
        break
    # increment the guess count by 1
    count_guess += 1
else:
    # if fail to guess in three turns
    print('You fail!')