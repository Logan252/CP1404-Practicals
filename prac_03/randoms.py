"""What did you see on line 1?
print(random.randint(5, 20))  # line 1

What was the smallest number you could have seen, what was the largest?
smallest number was 5, largest was 20

What did you see on line 2?
print(random.randrange(3, 10, 2))  # line 2

What was the smallest number you could have seen, what was the largest?
smallest number was 3, largest was 9

Could line 2 have produced a 4?
no, starts at 3 and can only go up by 2.

What did you see on line 3?
print(random.uniform(2.5, 5.5))

What was the smallest number you could have seen, what was the largest?
2.5 is the smallest, 5.5 is the largest

Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
import random

random_number = random.randint(1, 100)
print(random_number)
