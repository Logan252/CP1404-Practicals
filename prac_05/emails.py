"""Write a program that stores users' emails (unique keys) and names (values) in a dictionary
estimated time: 45 minutes
actual time: """


def main():
    """Create dictionary of emails-to-names."""
    email, email_to_name = get_email()
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/N) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_email():
    """get user to input email"""
    email_to_name = {}
    email = input("Email: ")
    return email, email_to_name


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    # many emails have numbers or birthdays attached, eg, logan.96@live.com.au, names dont contain numbers.
    name_parts = [part for part in parts if part.isalpha()]
    name = " ".join(name_parts).title()
    return name


main()