"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
# changed requirements form skeleton code as a password should not be below 8 characters
# changed special chars requirement to True
MIN_LENGTH = 8
MAX_LENGTH = 24
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for character in password:
        if character.islower():
            count_lower += 1
        elif character.isupper():
            count_upper += 1
        elif character.isdigit():
            count_digit += 1
        elif character in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False
    # and return False if it's zero
    # if we get here (without returning False), then the password must be valid

    print(f"you have:\n{count_lower} lower character(s)\n{count_upper} upper character(s)\n"
          f"{count_digit} number(s)\n{count_special} special character(s) ")
    return True


main()
