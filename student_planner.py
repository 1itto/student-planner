# Student Planner- Two group members
# Amnah Almutairi ID : 447200000
# Reemas Alsulami ID : 447201974
#section:78689

#Student planner is a program that allows students to store their multiple tasks and manage them by the highest priority, course, and due date.
#The program allows students to add, edit, delete, and mark tasks as completed. and provied a summary of their tasks.

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

 

def add_task(tasks, next_task_id):
    
    title = input("Task title: ").strip()
    while title == "":
        print("Error: Please enter a valid input.")
        title = input("Task title: ").strip()

    
    course = input("Course name: ").strip()
    while course == "":
        print("Error: Please enter a valid input.")
        course = input("Course name: ").strip()

    
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



def list_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks to display.")
        return
    print("--- All Tasks ---")
    for i in range(len(tasks)):
        task = tasks[i]
        if i > 0:
            print("-" * 40) 
        display_task(task)



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



def show_summary(tasks):
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["status"] == "Completed":
            completed += 1
    pending = total - completed
    
    if total == 0:
        percentage = 100
    else:
        percentage = completed / total * 100
    print("--- Task Summary ---")
    print(f"Total tasks: {total}")
    print(f"Pending tasks: {pending}")
    print(f"Completed tasks: {completed}")
    print(f"Completion percentage: {percentage:.1f}%")


# Shows the menu and runs each choice until the user exits

def main():
    tasks = []            
    next_task_id = 1      
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