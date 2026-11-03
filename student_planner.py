# Amnah Almutairi ID : 447200000
# Reemas Alsulami ID : 447200000

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

def add_task(tasks,next_task_id):
    title=read_required_text("Task title: ")
    course=read_required_text("Course name: ")
    due_date=read_due_date()
    priority=read_priority()

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

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def display_task(task):
    print(f"ID: {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Course: {task['course']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print(f"Status: {task['status']}")

def edit_task(tasks):
    task_id=task_id= read_task_id()
    if task_id is None:
        return
    task=find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return
    print("1.Title")
    print("2.Course")
    print("3.Due Date")
    print("4.Priority")
    print("5.Cancel")
    field_choice= input("Enter your choice: ").strip()
    if field_choice == "1":
        task["title"] = read_required_text("Task title: ")
    elif field_choice == "2":
        task["course"] = read_required_text("Course name: ")
    elif field_choice == "3":
        task["due_date"] = read_due_date()
    elif field_choice == "4":
        task["priority"] = read_priority()
    elif field_choice == "5":
        print("Edit canceled. The task was not changed.")
        return
    else:
        print("error: Invalid choice. Please select a valid option.")
        return
    print("Task updated successfully.")

def delete_task(tasks):
    task_id= read_task_id()
    if task_id is None:
        return
    task=find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
    else:
    tasks.remove(task)
    print(f"Task with ID {task_id} deleted successfully.")