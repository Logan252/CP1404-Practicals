"""Start time:8:30
   Estimated finish time: 12:00
   Actual finish time: 3:07
   (First 4 hours was done in another file by mistake, start time does not reflect accurately with commit times)"""

import datetime
from project import Project

FILE_NAME = "projects.txt"


def main():
    projects_list = load_projects(FILE_NAME)

    menu_choice = display_menu()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            projects_list = load_projects(FILE_NAME)
        elif menu_choice == 'S':
            save_projects(FILE_NAME, projects_list)
        elif menu_choice == 'D':
            display_projects(projects_list)
        elif menu_choice == 'F':
            filtered_projects_by_date(projects_list)
        elif menu_choice == 'A':
            add_project(projects_list)
        elif menu_choice == 'U':
            update_project(projects_list)
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
        file.readline()  # Skip the header line
        for line in file:
            name, start_date_str, priority, estimate, completion = line.strip().split('\t')
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            priority = int(priority)
            estimate = float(estimate)
            completion = int(completion)
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project.name}, Start date: {project.start_date.strftime('%d/%m/%Y')}, "
              f"Priority: {project.priority}, Estimate: ${project.estimate:.2f}, "
              f"Completion: {project.completion}%")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project.name}, Start date: {project.start_date.strftime('%d/%m/%Y')}, "
              f"Priority: {project.priority}, Estimate: ${project.estimate:.2f}, "
              f"Completion: {project.completion}%")


def update_project(projects):
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, Start date: {project.start_date.strftime('%d/%m/%Y')}, "
              f"Priority: {project.priority}, Estimate: ${project.estimate:.2f}, "
              f"Completion: {project.completion}%")

    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        new_completion_str = input("New Percentage: ")
        if new_completion_str.isdigit():
            new_completion = int(new_completion_str)
            project.completion = new_completion

        new_priority_str = input("New Priority: ")
        if new_priority_str.isdigit():
            new_priority = int(new_priority_str)
            project.priority = new_priority

        print(f"{project.name} updated.")
    else:
        print("Invalid choice.")


def filtered_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        filtered_projects.sort(key=lambda x: x.start_date)

        print("Filtered projects:")
        for project in filtered_projects:
            print(f"  {project.name}, Start date: {project.start_date.strftime('%d/%m/%Y')}, "
                  f"Priority: {project.priority}, Estimate: ${project.estimate:.2f}, "
                  f"Completion: {project.completion}%")
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")


def add_project(projects):
    print("Add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    priority_str = input("Priority: ")
    estimate_str = input("Cost estimate: $")
    completion_str = input("Percent complete: ")

    try:
        # if the slashes aren't inputted by the user, it has to finish inputting all the data to say it was invalid,
        # requires fixing.
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
        priority = int(priority_str)
        estimate = float(estimate_str)
        completion = int(completion_str)

        new_project = Project(name, start_date, priority, estimate, completion)
        projects.append(new_project)
        print(f"{new_project.name} added.")
    except ValueError:
        print("Invalid input format. Please enter valid values for priority, estimate, and completion.")


if __name__ == "__main__":
    main()
