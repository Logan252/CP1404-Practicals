"""There are some comments to help myself understand the code better, please feel free to add any info when marking"""

FILENAME = "name.txt"
out_file = open("name.txt", "w")
name = input("Please enter your name")
print(name, file=out_file)
# print("name is", name)
out_file.close()
# comments for self, above code opens file, takes input, uses print line to write to file then closes it.
# commented out code was to see if changes were applicable when file closes or when print line writes to the file.

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Name entered is", name)

# wanted to test 'a'. 'w' overwrites the file, 'a' append to the file.
# out_file = open("name.txt", "a")
# name = input("the second name entered is")
# print(name, file=out_file)
# out_file.close()

# using "with"
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Name entered is", name)

in_file = open("numbers.txt", "r")
total = 0
# question asks for first 2 numbers, for loop made sense
for line in range(2):
    numbers = int(in_file.readline())
    total += numbers
    # print(numbers) was just used to see what numbers were being selected during testing
print(total)
in_file.close()

# question asks for all numbers
in_file = open("numbers.txt", "r")
total = 0

for line in range(in_file):
    numbers = int(in_file.readline())
    total += numbers
    # print(numbers) was just used to see what numbers were being selected during testing
print(total)
in_file.close()
