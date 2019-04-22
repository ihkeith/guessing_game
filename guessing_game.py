# Information on list sorting was found here: https://docs.python.org/3.3/howto/sorting.html

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
    display_welcome()

    secret_number = random.randint(1, 10)
    player_guess = ""
    guesses = 0
    high_score = []
    play_a_game = input("Would you like to play? Yes/no  ")

    while play_a_game:
        player_guess = input("Please pick a number >  ")
        guesses += 1
        try:
            player_guess = int(player_guess)
            if player_guess <= 0:
                print("Please pick a number between 1 and 10.")
                continue
            elif player_guess > 10:
                print("Please pick a number between 1 and 10.")
                continue
            pass
        except ValueError:
            print("That isn't a valid number. Please try again.")
            continue
        if player_guess == secret_number:
            high_score.append(guesses)
            high_score.sort()
            print("Got it!")
            print("It took you {} guesses.".format(guesses))
            time.sleep(.5)
            play_a_game = input("Would you like to play again? Yes/no  ")
            if high_score:
                print("The current high score is {}".format(high_score[0]))
            if play_a_game.lower() == 'no':
                time.sleep(1)
                print("Thanks for playing; have a fantasic day!!")
                break
            else:
                guesses = 0
                secret_number = random.randint(1, 10)
        elif player_guess < secret_number:
            print("You guessed too low. The secret number is higher. Try again.")
            continue
        elif player_guess > secret_number:
            print("You guessed too high. The secret number is lower. Try again.")
            continue


if __name__ == '__main__':
    start_game()