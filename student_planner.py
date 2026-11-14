# Student Planner- Two group members
# Amnah Almutairi ID : 447200000
# Reemas Alsulami ID : 447200000
#section:78689

# Prints the menu the user sees before every choice

def display_menu():
    x = '-'
    print()
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
    print(x * 40)

 #Asks for the task details, checks them, then saves the new task in the list

def add_task(tasks, next_task_id):
    # The title can't be empty, so we keep asking until the user types something
    title = input("Task title: ").strip()
    while title == "":
        print("Error: Please enter a valid input.")
        title = input("Task title: ").strip()

    # Course name: ask again if it is empty
    course = input("Course name: ").strip()
    while course == "":
        print("Error: Please enter a valid input.")
        course = input("Course name: ").strip()

    # The date has to look like 15/10/2026: two digits, two digits, then four digits
    while True:
        dates = input("Due date (DD/MM/YYYY): ").strip()
        date = dates.split("/")   
        if len(date) == 3 and (len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4):
            if date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
                break
            else:
                print("Error: Please enter a valid date.")
        else:
            print("Error: Please enter a valid date.")
    due_date = dates

    # Priority: 1, 2, or 3 is saved as High, Medium, or Low
    while True:
        value = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        if value == "1":
            priority = "High"
            break
        elif value == "2":
            priority = "Medium"
            break
        elif value == "3":
            priority = "Low"
            break
        else:
            print("Error: Enter 1 for High, 2 for Medium, or 3 for Low")

    # A new task is always Pending until the user marks it as completed
    new_task = {
        "id": next_task_id,
        "title": title,
        "course": course,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(new_task)
    print(f"Task added successfully. Task ID: {next_task_id}")
    return next_task_id + 1

# Goes through the list and gives back the task with this ID, or None if it isn't there

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

# Prints one task's details; we use it everywhere so tasks always look the same

def display_task(task):
    print(f"ID: {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Course: {task['course']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print(f"Status: {task['status']}")

# Lets the user change one part of a task. The ID and status never change here

def edit_task(tasks):
    # The ID must be a positive whole number, so things like abc, 0 or -1 are rejected
    value = input("Enter task ID: ").strip()
    if not (value.isdigit() and int(value) > 0):
        print("Error: Invalid task ID.")
        return
    task_id = int(value)
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return

    print("1. Title")
    print("2. Course")
    print("3. Due date")
    print("4. Priority")
    print("5. Cancel")
    # Ask which part of the task they want to change
    field_choice = input("Enter your choice: ").strip()

    if field_choice == "1":
        title = input("Task title: ").strip()
        while title == "":
            print("Error: Please enter a valid input.")
            title = input("Task title: ").strip()
        task["title"] = title

    elif field_choice == "2":
        course = input("Course name: ").strip()
        while course == "":
            print("Error: Please enter a valid input.")
            course = input("Course name: ").strip()
        task["course"] = course

    elif field_choice == "3":
        while True:
            dates = input("Due date (DD/MM/YYYY): ").strip()
            date = dates.split("/")
            if len(date) == 3 and (len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4):
                if date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
                    break
                else:
                    print("Error: Please enter a valid date.")
            else:
                print("Error: Please enter a valid date.")
        task["due_date"] = dates

    elif field_choice == "4":
        while True:
            value = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
            if value == "1":
                priority = "High"
                break
            elif value == "2":
                priority = "Medium"
                break
            elif value == "3":
                priority = "Low"
                break
            else:
                print("Error: Enter 1 for High, 2 for Medium, or 3 for Low")
        task["priority"] = priority

    elif field_choice == "5":
        print("Edit canceled. The task was not changed.")
        return

    else:
        print("Error: Invalid choice. Please select a valid option.")
        return

    print("Task updated successfully.")

# Removes the task with the given ID from the list

def delete_task(tasks):
    value = input("Enter task ID: ").strip()
    if not (value.isdigit() and int(value) > 0):
        print("Error: Invalid task ID.")
        return
    task_id = int(value)
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
    else:
        tasks.remove(task)
        print(f"Task with ID {task_id} deleted successfully.")

# Shows every task in the same order they were added

def list_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks to display.")
        return
    print("--- All Tasks ---")
    for i in range(len(tasks)):
        task = tasks[i]
        if i > 0:
            print("-" * 40) # a line of dashes between tasks so they're easier to read
        display_task(task)

# Shows the tasks of one course. We compare in lowercase so CSC111 and csc111 match

def list_tasks_by_course(tasks):
    if len(tasks) == 0:
        print("No tasks to display.")
        return
    course = input("Enter course name or code: ").strip()
    while course == "":
        print("Error: Please enter a valid input.")
        course = input("Enter course name or code: ").strip()
    found = False
    for task in tasks:
        if task["course"].lower() == course.lower():
            if found:
                print("-" * 40)
            display_task(task)
            found = True
    if not found:
        print(f"No tasks found for course {course}.")

# Shows only the tasks that have the priority the user picked

def list_tasks_by_priority(tasks):
    if len(tasks) == 0:
        print("No tasks to display.")
        return
    while True:
        value = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        if value == "1":
            priority = "High"
            break
        elif value == "2":
            priority = "Medium"
            break
        elif value == "3":
            priority = "Low"
            break
        else:
            print("Error: Enter 1 for High, 2 for Medium, or 3 for Low")
    found = False
    for task in tasks:
        if task["priority"] == priority:
            if found:
                print("-" * 40)
            display_task(task)
            found = True
    if not found:
        print(f"No tasks found with {priority} priority.")

# Changes a task to Completed, unless it's already completed

def mark_task_completed(tasks):
    value = input("Enter task ID: ").strip()
    if not (value.isdigit() and int(value) > 0):
        print("Error: Invalid task ID.")
        return
    task_id = int(value)
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
    elif task["status"] == "Completed":
        print(f"Task {task_id} is already completed.")
    else:
        task["status"] = "Completed"
        print(f"Task {task_id} marked as completed.")

# Counts the tasks and works out how many are done as a percentage

def show_summary(tasks):
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["status"] == "Completed":
            completed += 1
    pending = total - completed
    # If there are no tasks we can't divide by zero, so we just show 100%
    if total == 0:
        percentage = 100
    else:
        percentage = completed / total * 100
    print("--- Task Summary ---")
    print(f"Total tasks: {total}")
    print(f"Pending tasks: {pending}")
    print(f"Completed tasks: {completed}")
    print(f"Completion percentage: {percentage:.1f}%")

# Runs the program: shows the menu, does what the user picks, and repeats until they choose 10

def main():
    tasks = []            # we start with no tasks every time the program runs
    next_task_id = 1      # this only goes up, so a deleted ID is never used again
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            next_task_id = add_task(tasks, next_task_id)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            value = input("Enter task ID: ").strip()
            if value.isdigit() and int(value) > 0:
                task_id = int(value)
                task = find_task_by_id(tasks, task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found.")
                else:
                    print("--- Task Details ---")
                    display_task(task)
            else:
                print("Error: Invalid task ID.")
        elif choice == "5":
            list_all_tasks(tasks)
        elif choice == "6":
            list_tasks_by_course(tasks)
        elif choice == "7":
            list_tasks_by_priority(tasks)
        elif choice == "8":
            mark_task_completed(tasks)
        elif choice == "9":
            show_summary(tasks)
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice.")

 #Start the program           
main()   