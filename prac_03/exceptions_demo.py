"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ValueError occurs when a non integer is entered during the input for the numerator and denominator.
2. When will a ZeroDivisionError occur?
Zero divison error occurs only when input from the denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
if statement within the try, if 0 is given, the block starts again as is_valid_input remains false
until the else block.
"""
# standard exception handling pattern
is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("denominator cannot be 0")
        else:
            is_valid_input = True
            fraction = numerator / denominator
            # Instead of having 2 print lines
            print(f"{fraction}\nFinished")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    # print("Cannot divide by zero!")
