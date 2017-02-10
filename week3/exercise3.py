from __future__ import division, print_function
import random


def super_asker(low, high):
    """
    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Give me a number between {low} and {high}:".format(low=low,
                                                                  high=high)
    while True:
        user_input = ""
        input_number = ""
        user_input = raw_input(message)
        try:
            input_number = int(user_input)
            if low <= input_number <= high:
                print("Thanks, {} looks good!".format(input_number))
                return input_number
            else:
                print("{} isn't between {} and {}!".format(input_number,
                                                           low,
                                                           high))
        except:
            print("{} isn't a number! try again:".format(user_input))


def not_number_rejector(message):
    while True:
        user_input = raw_input(message)
        try:
            int(user_input)  # try it to trigger failure
            print("Thanks, {} looks good!".format(user_input))
            return int(user_input)
        except:
            print("{} isn't a number! try again:".format(user_input))


def advancedGuessingGame():
    """
    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nwelcome to the guessing game!")
    lowerBound = int(not_number_rejector("Enter an lower bound: "))
    upperBound = int(not_number_rejector("Enter an upper bound: "))
    if lowerBound > upperBound:
        print("your range is inverted")
        upperBound = int(not_number_rejector("Enter an upper bound: "))
    if upperBound == lowerBound or upperBound == lowerBound + 1:
        print("your range is too small")
        upperBound = int(not_number_rejector("Enter an upper bound: "))
    print("Guess a number between {} and {} ?".format(lowerBound, upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = super_asker(lowerBound, upperBound)
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
    advancedGuessingGame()
