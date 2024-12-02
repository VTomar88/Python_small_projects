"""
Quiz Game

This script implements a simple multiple-choice quiz game. The user is presented with 
randomized questions, selects an answer, and receives feedback on whether their response 
is correct. The game tracks the user's score and displays it at the end.

Modules:
    - random: Used to shuffle the quiz questions for randomness.
    - termcolor: Used to print colored feedback for correct and incorrect responses.

Constants:
    - QUESTION: Key for the question text in each quiz item.
    - OPTIONS: Key for the list of answer options in each quiz item.
    - RESPONSE: Key for the correct answer in each quiz item.
"""

import random
from termcolor import cprint

# Keys for the quiz dictionary
QUESTION = 'question'
OPTIONS = 'options'
RESPONSE = 'response'


def ask_question(index, question, options):
    """
    Display a question and its options, and prompt the user for a response.

    Args:
        index (int): The question number.
        question (str): The question text.
        options (list of str): The list of answer options.

    Returns:
        str: The user's response as an uppercase single character.
    """
    print(f"Question {index}. {question}")
    for option in options:
        print(option)

    # Prompt user for a response and ensure it's in uppercase
    return input('Your response (a/b/c/d): ').upper().split()[0]


def run_game(quiz):
    """
    Run the quiz game by presenting randomized questions and evaluating responses.

    Args:
        quiz (list of dict): The quiz questions, each containing:
            - QUESTION: The question text.
            - OPTIONS: The list of answer options.
            - RESPONSE: The correct answer.

    Returns:
        None
    """
    # Shuffle the quiz questions for randomness
    random.shuffle(quiz)

    score = 0  # Initialize score

    # Iterate through each question in the quiz
    for index, item in enumerate(quiz, 1):
        response = ask_question(index, item[QUESTION], item[OPTIONS])

        # Check if the response is correct
        if response == item[RESPONSE]:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint('Your response is wrong!', 'red')
        print()  # Print a blank line for readability

    # Display the final score
    print(f"Game over! Your score is {score} out of {len(quiz)}")


def main():
    """
    Main function to initialize the quiz and start the game.

    Returns:
        None
    """
    # Define the quiz questions
    quiz = [
        {QUESTION: 'What is the capital of France?',
         OPTIONS: ['A. Berlin', 'B. Washington', 'C. Paris', 'D. Moscow'],
         RESPONSE: 'C'
         },
        {QUESTION: 'Which is called the red planet?',
         OPTIONS: ['A. Mars', 'B. Earth', 'C. Jupiter', 'D. Venus'],
         RESPONSE: 'A'
         },
        {QUESTION: 'Which is the largest ocean?',
         OPTIONS: ['A. Atlantic', 'B. Pacific', 'C. Indian Ocean', 'D. Arctic'],
         RESPONSE: 'B'
         }
    ]

    # Start the game
    run_game(quiz)


if __name__ == '__main__':
    main()
