# Rock Paper Scissor game 
import random

# List of items stored in immutable tuple 
item_list = ('r', 'p', 's')
# Loop
while True:
    # Ask user to choose from (r)ock, (p)aper, (s)cissor
    user_input = input('Rock, Paper, Scissor? (r/p/s): ')
    
    # Computer to choose between r, p, s
    comp_guess = random.choices(item_list)[0]

    # Convert user input into a value
    if user_input == 'r':
        item_name = "🪨"
    elif user_input == 'p':
        item_name = '📄'
    elif user_input == 's':
        item_name = '✂'

    # Convert computer guess into a value
    if comp_guess == 'r':
        comp_name = "🪨"
    elif comp_guess == 'p':
        comp_name = '📄'
    elif comp_guess == 's':
        comp_name = '✂'


    # if user = r or p or s
    if user_input in item_list:
        # print what user choose
        print(f'You chose {item_name}')   
         # print what computer choose
        print(f'Computer choose {comp_name}')
        # if user = computer -> tie
        if comp_guess == user_input:
            print("Its a tie!")
        # else if user = r/s/p and computer p/r/s -> user lose
        if (user_input=='r' and comp_guess=='p') or (user_input=='s' and comp_guess=='r') or (user_input=='p' and comp_guess=='s'):
            print('You lose')
        # else if user = p/r/s and user r/s/p 
        if (user_input=='p' and comp_guess=='r') or (user_input=='r' and comp_guess=='s') or (user_input=='s' and comp_guess=='p'):
            print('You win')
    # else invalid option
    else:
        print('Invalice chocie!')
        continue # skip rest if the choice is invlid and reach the top level of the loop
    # wish to continue -  no break
    continue_ask = input('Continue? (y/n): ').lower()
    if continue_ask == 'n':
        break