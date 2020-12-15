"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random



def get_guess():
    while True:
        guess = input("Guess a number between one and ten!    ")
        try:
            guess = int(guess)
        except ValueError:
            print("Oops! Try using an integer instead!")
        else:
            return guess
        

def start_game():
    print("Welcome to the guessing game!")
    solution = random.randint(1, 10)
    guess = 1000
    attempts = 0
    while guess != solution:
        guess = get_guess()
        attempts += 1
        if guess > solution:
            print("Try guessing lower.    ")   
        elif guess < solution:
            print("Try guessing higher.    ")
            
    
    print("Hey, you got it right! And in only {} attempts, too. Thanks for playing!".format(attempts))

start_game()