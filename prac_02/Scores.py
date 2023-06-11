"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(give_grade(score))
    # don't want an Invalid score, below comments is exploratory
    # while give_grade(score) == "Invalid score":
    # score = float(input("Enter score: "))
    # print(give_grade(score))


def give_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"

    elif 50 <= score < 90:
        return "Passable"

    elif score >= 90:
        return "Excellent"

    else:
        return "Bad"


main()
