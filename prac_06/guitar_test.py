"""Test program for guitar class program
    This form of testing is quite 'manual' since we need to read the output and compare it ourselves"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def run_tests():
    # Test input from coder to check classes functionality
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    # The numbers 101 and 11 are from current year - age they come out.
    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()
