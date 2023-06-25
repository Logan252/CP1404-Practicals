"""Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS"""
import random

MINIMUM_LINES = 1
MAXIMUM_LINES = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_LINES, MAXIMUM_LINES)
            while number in quick_pick:
                number = random.randint(MINIMUM_LINES, MAXIMUM_LINES)
            quick_pick.append(number)
        print(f"{quick_pick[0]} {quick_pick[1]} {quick_pick[2]} {quick_pick[3]} {quick_pick[4]} {quick_pick[5]}")


main()
