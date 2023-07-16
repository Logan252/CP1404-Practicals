"""Start time: 1:20
    Finish time: """
CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
