# Rock Paper Scissor game 
# Varsha Tomar 15 Nov 2024
import random

# List of items stored in immutable tuple 
item_list = ('r', 'p', 's')

# Dict to store emojis for items
emojis = {"r": "🪨", "p": "📄", "s": "✄"}

# counter for scoring
wins = 0
loses = 0
ties = 0

# Loop
while True:
    # Ask user to choose from (r)ock, (p)aper, (s)cissor
    user_input = input('Rock, Paper, Scissor? (r/p/s): ')
    
    # Computer to choose between r, p, s
    comp_guess = random.choices(item_list)[0]

    # if user = r or p or s
    if user_input in item_list:
        # print what user choose
        print(f'You chose {emojis[user_input]}')   
         # print what computer choose
        print(f'Computer choose {emojis[comp_guess]}')
        # if user = computer -> tie
        if comp_guess == user_input:
            print("Tie!")
            ties += 1
        # else if user = p/r/s and user r/s/p 
        elif ((user_input=='p' and comp_guess=='r') or 
              (user_input=='r' and comp_guess=='s') or 
              (user_input=='s' and comp_guess=='p')):
            print('You Win')
            wins += 1
        else:
            print('You Lose')
            loses += 1
    # else invalid option
    else:
        print('Invalice chocie!')
        continue # skip rest if the choice is invlid and reach the top level of the loop
    # wish to continue -  no break
    continue_ask = input('Continue? (y/n): ').lower()
    if continue_ask == 'n':
        # Display the final score
        print(f'\nFinal score: Wins: {wins}, Loses: {loses}, Ties: {ties}')
        break