#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 26, 2022
# This program outputs the sum of all numbers preceding the user's
# number using a while loop.


def main():

    # Tries to get the user's number as an integer.
    try:
        user_number = int(input("Enter a positive integer: "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Restarts the program if the user entered a negative number
    if user_number < 0:
        print("You must enter a positive integer. Please try again.")

    # Initializing counter and sum variables
    counter = 0
    sum = 0

    # Code executed continually until user_number is equal to counter
    while user_number >= counter and user_number >= 0:
        sum = sum + counter
        print(f"Looped through {counter} times.")
        counter += 1

    # Outputs the sum of all numbers that precede the user's number

    if user_number >= 0:
        print(
            f"The sum of the consecutive positive integers preceding {user_number} is {sum}."
        )


if __name__ == "__main__":
    main()
