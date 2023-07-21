"""start time: 12:30
    End time: 1:16"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    # didn't require all languages but already had them in the program
    java = ProgrammingLanguage("Java", "Dynamic", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Static", True, 1995)

    languages = [java, c_plus_plus, visual_basic, python, ruby]
    print("Dynamic typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("Static typed languages are:")
    for language in languages:
        if language.is_static():
            print(language.name)


main()
