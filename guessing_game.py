"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random, time

def display_welcome():
    time.sleep(.5)
    print("=" * 71)
    time.sleep(.5)
    print("Welcome to the Number Counting Game!")
    time.sleep(1)
    print("Pick a number between 1 and 10.")
    time.sleep(1)
    print("We'll let you know if you guess too high or too low.")
    time.sleep(1)
    print("Good Luck!!!!!")
    time.sleep(.5)
    print("=" * 71)


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    display_welcome()

    secret_number = random.randint(1, 10)
    player_guess = ""
    guesses = 0

    while player_guess != secret_number:
        player_guess = input("Please pick a number >  ")
        guesses += 1
        try:
            player_guess = int(player_guess)
            pass
        except ValueError as err:
            print("That isn't a valid number. Please try again.")
            continue
        if player_guess == secret_number:
            print("Got it!")
            print("It took you {} guesses.".format(guesses))
            time.sleep(.5)
            print("Thanks for playing; have a fantasic day!!")
            break
        elif player_guess < secret_number:
            print("You guessed too low. The secret number is higher. Try again.")
            continue
        elif player_guess > secret_number:
            print("You guessed too high. The secret number is lower. Try again.")
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function
    start_game()