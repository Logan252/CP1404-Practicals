"""Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS"""
import random

LOWEST_QUICK_PICK_NUMBER = 1
HIGHEST_QUICK_PICK_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(LOWEST_QUICK_PICK_NUMBER, HIGHEST_QUICK_PICK_NUMBER)
            # to keep all line numbers different
            while number in quick_pick:
                number = random.randint(LOWEST_QUICK_PICK_NUMBER, HIGHEST_QUICK_PICK_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        # number will never be higher than 2 digits
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
