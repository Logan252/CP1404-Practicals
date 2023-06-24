def get_numbers():
    numbers = []
    # in this situation would 'i' be a better name than number for the range line?
    for number in range(5):
        number = int(input("please enter a number"))
        numbers.append(number)

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


def check_username():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("please enter a username")
    if username in usernames:
        print("Access granted")
    else:
        print("Access Denied")


get_numbers()
check_username()
