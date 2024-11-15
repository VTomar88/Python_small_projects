# Rock Paper Scissor game 
# Varsha Tomar 15 Nov 2024
import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

# Dict to store emojis for items
emojis = {ROCK: "🪨", PAPER: "📄", SCISSOR: "✄"}

# List of items stored in immutable tuple 
item_list = tuple(emojis.keys())

# counter for scoring
game_wins = 0
game_loses = 0
game_ties = 0

def display_choices(user_input, comp_guess):
    # print what user choose
    print(f'You chose {emojis[user_input]}')   
        # print what computer choose
    print(f'Computer choose {emojis[comp_guess]}')

def compare_results(user_input, comp_guess):
    global game_loses, game_wins, game_ties
    # if user = computer -> tie
    if comp_guess == user_input:
        print("Tie!")
        game_ties += 1
    # else if user = p/r/s and user r/s/p 
    elif ((user_input==PAPER and comp_guess==ROCK) or 
        (user_input==ROCK and comp_guess==SCISSOR) or 
        (user_input==SCISSOR and comp_guess==PAPER)):
        print('You Win')
        game_wins += 1
    else:
        print('You Lose')
        game_loses += 1

def game_continue_ask():
    global game_wins, game_loses, game_ties
    # wish to continue -  no break
    while True:
        continue_ask = input('Continue? (y/n): ').lower()
        if continue_ask == 'n':
            # Display the final score
            print(f'\nFinal score: Wins: {game_wins}, Loses: {game_loses}, Ties: {game_ties}')
            return False
        elif continue_ask == 'y':
            return True
        else:
            print("Enter only 'y' for yes or 'n' for no.")

def compare_user_input(comp_guess):
    while True:
        # Ask user to choose from (r)ock, (p)aper, (s)cissor
        user_input = input('Rock, Paper, Scissor? (r/p/s): ') 
        # if user = r or p or s
        if user_input in item_list:
            display_choices(user_input, comp_guess)
            compare_results(user_input, comp_guess)
            break      
        # else invalid option
        else:
            print('Invalice chocie!')

def play_game():
    while True:               
        # Computer to choose between r, p, s
        comp_guess = random.choices(item_list)[0]
        # compare the resuts and play the game
        compare_user_input(comp_guess)
       # ask user if wish to continue the game
        if not game_continue_ask():
            break

# Play the game
if __name__ == "__main__":
    play_game()