NAME_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "b0bf1a", "AliceBlue": "f0f8ff",
                  "Amaranth": "e52b50", "Amber": "ffbf00", "Amethyst": "9966cc", "beige": "f5f5dc",
                  "Black": "000000", "Carmine": "960018"}

colour_name = input("enter a colour name").lower()

while colour_name != "":
    matching_names = []
    colour_code = None

    for name in NAME_TO_COLOUR:
        if name.lower() == colour_name.lower():
            matching_names.append(name)
            colour_code = NAME_TO_COLOUR[name]

    if colour_code is None:
        print("Sorry, that code is not in this dictionary")
    else:
        for name in matching_names:
            print(f"The hexadecimal code for {colour_name} is {NAME_TO_COLOUR.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()
