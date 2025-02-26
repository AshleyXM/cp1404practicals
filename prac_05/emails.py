"""
Emails
Estimate: 20 minutes
Actual:   32 minutes
"""

INDEX_NAME = 0

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name_from_email(email)
        ans = input(f"Is your name {full_name}? (Y/n) ").upper()
        if ans == "Y" or ans == "":
            email_to_name[email] = full_name
        else:
            name = input("Name: ")
            email_to_name[email] = name

        email = input("Email: ")

    print()
    display_name_and_email(email_to_name)

def extract_name_from_email(email):
    """Extract full name from email"""
    email_name = email.split("@")[INDEX_NAME]
    name_parts = email_name.split(".")
    full_name = " ".join([part.title() for part in name_parts])
    return full_name


def display_name_and_email(email_to_name):
    """Display full name and email"""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()