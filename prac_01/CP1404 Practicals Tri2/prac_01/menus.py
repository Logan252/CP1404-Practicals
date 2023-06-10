name = input("Enter name")
print("(H)ello,\n(G)oodbye,\n(Q)uit")
# self marking, originally didn't have the MENU_STRING, added after revising suggested solutions.
menu_choice = input(">>>").upper()
MENU_STRING = "(H)ello,\n(G)oodbye,\n(Q)uit"

while menu_choice != 'Q':
    if menu_choice == 'H':
        print("hello", name)
        print(MENU_STRING)
        menu_choice = input(">>>").upper()
    elif menu_choice == 'G':
        print("goodbye", name)
        print(MENU_STRING)
        menu_choice = input(">>>").upper()
    else:
        print("Invalid choice")
        print(MENU_STRING)
        menu_choice = input(">>>").upper()
print("Finished.")
