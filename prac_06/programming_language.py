"""Programming Language class"""


# Some docstrings or comments may seem unnecessary through the program but are used for future study.

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """is_dynamic() - which returns True/False if the programming language is dynamically typed or not Note: it's
        really important that you understand this function will take no parameters (other than self). The information
        is already stored inside the object, so you don't need to tell the object its own data. """
        return self.typing == "Dynamic"

    def is_static(self):
        """Practice, not actually required for prac"""
        return self.typing == "Static"


def run_tests():
    """Checked solutions once completed and noticed test was here,
     is this standard practice or should be removed on a finished project?
      Or I may have misunderstood the instructions"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [visual_basic, python, ruby]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()