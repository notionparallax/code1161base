from __future__ import division, print_function
import random


def exampleGuessingGame():
    """
    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = raw_input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(raw_input("guess a number: "))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
