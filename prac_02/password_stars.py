"""
Copy password_stars.py that you wrote earlier from Sandbox into your prac_02 folder and commit
(with a message like "Add password check program")v
"""

min_length = 8


def main():
    password = get_password(min_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Please enter password of at least {} characters: ".format(min_length))
    while len(password) < minimum_length:
        password = input("Please enter password of at least {} characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()