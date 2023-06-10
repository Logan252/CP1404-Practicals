"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# self marking, suggested answer has if instead of while loop, if this matters please provide feedback during marking
score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if 50 < score < 90:
    print("Passable")
elif score >= 90:
    print("Excellent")
else:
    print("Bad")
