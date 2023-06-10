# part c differs from the recommended solution but same output
for i in range(1, 21, 2):
    print(i, end=' ')
print()
# exercise a
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# exercise b
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# exercise c
num_of_stars = int(input("Please enter number of stars"))
for i in range(num_of_stars):
    print(end='*')
print()
# exercise d
num_of_stars = int(input("Please enter number of stars"))
for i in range(1, num_of_stars + 1):
    print('*' * i)
print()
