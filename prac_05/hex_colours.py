NAME_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "b0bf1a", "AliceBlue": "f0f8ff",
                  "Amaranth": "e52b50", "Amber": "ffbf00", "Amethyst": "9966cc", "beige": "f5f5dc",
                  "Black": "000000", "Carmine": "960018"}

colour_name = input("enter a colour name").lower()

while colour_name != "":
    matching_names = [name for name in NAME_TO_COLOUR if name.lower() == colour_name.lower()]
    if len(matching_names) == 0:
        print("Sorry, that code is not in this dictionary.")
    else:
        for name in matching_names:
            print(f"The hexadecimal code for {name} is {NAME_TO_COLOUR[name]}.")

    colour_name = input("Enter a colour name: ")


