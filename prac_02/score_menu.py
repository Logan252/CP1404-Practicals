MENU_STRING = "(G)et a valid score,\n(P)rint result,\n(S)how stars,\n(Q)uit"
NO_SCORE_ERROR_MESSAGE = "Score not provided. Please select 'G' to get a valid score."


def main():
    print(MENU_STRING)
    menu_choice = input(">>>").upper()
    score = None

    while menu_choice != 'Q':
        if menu_choice == 'G':
            score = get_score()
        elif menu_choice == 'P':
            if score is not None:
                result = give_grade(score)
                print("Result:", result)
            else:
                print(NO_SCORE_ERROR_MESSAGE)
        elif menu_choice == 'S':
            if score is not None:
                print_asterisk(score)
            else:
                print(NO_SCORE_ERROR_MESSAGE)
        else:
            print("Invalid choice")

        print(MENU_STRING)
        menu_choice = input(">>>").upper()

    print("Some kind of farewell.")


# (G)et a valid score (must be 0-100 inclusive)
def get_score():
    while True:
        try:
            score = float(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")


# (P)rint result (copy or import your function to determine the result from score.py)
def give_grade(score):
    if 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


# (S)how stars (this should print as many stars as the score)
def print_asterisk(score):
    print('*' * int(score))


main()
