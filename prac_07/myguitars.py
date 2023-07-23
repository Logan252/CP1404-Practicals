""" Script to add, organise and read guitars from CSV file.
    Start time: 11:03
    Finish time: ......"""


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year


# Function to read guitars from the file and store them in a list of Guitar objects
def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def add_guitars(guitars):
    name = input("Please enter a guitar name")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add.name, "added.")
        name = input("Please enter a guitar name")


def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, ${guitar.cost}")


if __name__ == "__main__":
    file_name = "guitars.csv"
    guitars_list = read_guitars_from_file(file_name)

    # Sort by oldest to newest
    guitars_list.sort()

    print("\nGuitars list sorted by year (oldest to newest):\n")
    display_guitars(guitars_list)

    add_guitars(guitars_list)

    print("\nAll Guitars (including new ones):\n")
    display_guitars(guitars_list)

    with open(file_name, 'w') as out_file:
        for guitar in guitars_list:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")