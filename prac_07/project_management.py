""" Start time: 1:00
    expected finish time: 5:15
    Actual finish time:"""

# Use the datetime module for the project start date
import datetime
# Note for self, CP1404 must be open, not just prac_07 for import to work
from prac_07.project import Project

FILE_NAME = "projects.txt"


def main():
    projects_list = load_projects(FILE_NAME)
    menu_choice, menu_string = display_menu()
    while menu_choice != 'Q':
        if menu_choice == 'L':

        elif menu_choice == 'S':


        elif menu_choice == 'D':

        elif menu_choice == 'F':

        elif menu_choice == 'A':

        elif menu_choice == 'U':

        else:
            print("Invalid menu choice")

        menu_choice = display_menu()


def display_menu():
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    menu_choice = input(">>> ").upper()
    return menu_choice


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            name, start_date_str, priority, estimate, completion = line.strip().split('\t')
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            priority = int(priority)
            estimate = float(estimate)
            completion = int(completion)
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename):
    pass


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def sort_projects():
    pass


def add_project():
    pass


if __name__ == "__main__":
    main()
