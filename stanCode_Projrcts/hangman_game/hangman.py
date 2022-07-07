"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Hangman game.
    If player guessed wrong 7 times, game over.
    If player guessed the word right, he wins.
    """
    answer = random_word()
    wrong_guesses = N_TURNS
    revealed_words = str('-'*len(answer))

    print('The word looks like ' + str(revealed_words))
    print('You have ' + str(wrong_guesses) + ' wrong guesses left.')

    while True:


        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        if len(input_ch) == 1:
            if input_ch.isalpha():

                if answer.find(input_ch) != -1:
                    # when player guessed right
                    print('You are Correct!')


                    for i in range(len(answer)):
                        # replace string when guessed right
                        if input_ch == answer[i]:
                            revealed_words = revealed_words[:i] + input_ch + revealed_words[(i+1):]
                    print('The word looks like ' + str(revealed_words))
                    print('You have ' + str(wrong_guesses) + ' wrong guesses left.')


                    if revealed_words.find('-') == -1:
                        # Player wins
                        print('You win!!')
                        print('The word was: '+str(answer))
                        break
                else:
                    # when player guessed wrong
                    print('There is no ' + str(input_ch) + '\'s in the word.')
                    wrong_guesses -= 1

                    print('The word looks like ' + str(revealed_words))
                    print('You have ' + str(wrong_guesses) + ' wrong guesses left.')

                    if wrong_guesses == 0:
                        # game over
                        print('You are completely hung :(')
                        print('The word was: ' + str(answer))
                        break
            else:
                print('Illegal format.')
        else:
            print('Illegal format.')




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
