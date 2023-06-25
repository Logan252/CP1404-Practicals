numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3, 1, 4,1,5,9
# numbers[3:4] = 1, 5      Incorrect, correct answer is [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers)
# 1.
numbers[0] = "ten"
print(numbers)
# 2.
numbers[-1] = 1
print(numbers)
# 3.
print(numbers[2:])
# numbers value hasnt changed, if wanted to change could save to a new list or overwrite current list
print(numbers)
# 4.Print whether 9 is an element of numbers
print(9 in numbers)
