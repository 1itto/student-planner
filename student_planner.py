# Amnah Almutairi ID : 447200000
# Reemas ID : 447200000

def display_menu():
    x = '-'
    print("STUDENT PLANNER")
    print(x * 40)
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Find a task by ID")
    print("5. List all tasks")
    print("6. List tasks by course")
    print("7. List tasks by priority")
    print("8. Mark a task as completed")
    print("9. View task summary")
    print("10. Exit")
    print("11. Search tasks by title keywords (three-member groups only)")
    print(x * 40)

def user_input(text):
    value = input(text.strip())
    while value == "":
        print("Error: Please enter a valid input.")
        value = input(text.strip())
    return value