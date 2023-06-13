# self marking, total_price was originally after while loop, suggested solution has it as before, assuming
# the reasoning is that set values should be at the start of the program
total_price = 0
number_of_items = int(input("Please enter the number of items: "))
while number_of_items < 0:
    print("invalid number of items")
    number_of_items = int(input("Please enter the number of items: "))

for i in range(1, number_of_items + 1):
    price = float(input(f"Please enter the price of item {i}: "))
    total_price += price
if total_price > 100:
    print("You qualify for a 10% discount!")
    total_price *= 0.9
print(f"The total price for {number_of_items} items is: ${total_price:.2f}")
