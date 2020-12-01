#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program is a guessing game

import constants


def main():
    # this function compares a user input to a constant

    print("Today we will play a guessing game.")

    # input
    user_guess = int(input("Enter a number between 0-9: "))
    print("")

    # process if correct
    if user_guess == constants.CORRECT_GUESS:
        # output
        print("Correct! {} was the right answer."
              .format(constants.CORRECT_GUESS))

    # process if incorrect
    if user_guess != constants.CORRECT_GUESS:
        # output
        print("Incorrect, try again!")


if __name__ == "__main__":
    main()
