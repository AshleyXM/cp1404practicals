"""
Estimated time:
Actual time:
"""
from project import Project

FILENAME = 'projects.txt'

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l': # load projects
            pass
        elif choice == 's': # save projects
            pass
        elif choice == 'd': # display projects
            handle_display_projects(projects)
        elif choice == 'f': # filter projects by date
            pass
        elif choice == 'a': # add new project
            handle_add_project(projects)
        elif choice == 'u': # update project
            handle_update_project(projects)
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").lower()


def load_projects(filename=FILENAME):
    """Load projects from file"""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        # name, start date, priority, cost, completion percentage
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def display_menu():
    """Display menu"""
    print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")


def handle_display_projects(projects):
    """Handle displaying projects"""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort()
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def handle_update_project(projects):
    """Handle updating projects"""
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    # TODO: Error check the input choice
    current_project = projects[choice]
    print(current_project)
    set_project_info(current_project, 'percentage')
    set_project_info(current_project, 'priority')


def set_project_info(project, info):
    """Set new percentage or priority for project"""
    new_info = input(f"New {info.title()}: ")
    if new_info != '':
        if info == 'percentage':
            project.set_percentage(int(new_info))
        elif info == 'priority':
            project.set_priority(int(new_info))


def handle_add_project(projects):
    """Handle adding new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percentage = int(input("Percentage complete: "))
    new_project = Project(name, start, priority, cost, percentage)
    projects.append(new_project)


main()