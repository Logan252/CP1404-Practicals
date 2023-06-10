"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# self marking, code matched version 2, logic behind was that a store can make 0 in sales in a day,
# can be useful data for stats i.e an employee may have done 0 sales on shift.
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print(f"bonus is: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))
    else:
        bonus = sales * 0.15
        print(f"bonus is: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))
