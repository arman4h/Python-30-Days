file_path = "task.txt"


def footer():
    print("\n0. Main Menu")
    print("1. Exit")
    choice = input("Selection: ")

    if choice == "0":
        main()
    elif choice == "1":
        print("Have a good day!")
    else:
        print("Invalid choice!")
        footer()


def add_task():
    name = input("Task Name: ").strip()
    status = input("Status (Pending/Completed): ").strip()

    if name == "" or status == "":
        print("Fields cannot be empty!")
        return

    count = 0

    try:
        with open(file_path, "r") as file:
            for _ in file:
                count += 1
    except FileNotFoundError:
        pass

    task_id = count + 1

    with open(file_path, "a") as file:
        file.write(f"{task_id}|{name}|{status}\n")

    print("✅ Task added successfully!")
    footer()


def view_task():
    print("\n##### All Tasks #####")

    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No tasks found.")

    print("##### End #####")


def update_task():
    view_task()

    task_id = input("Enter Task ID to update: ")

    if not task_id.isdigit():
        print("Invalid ID!")
        return

    task_id = int(task_id)

    tasks = []
    found = False

    with open(file_path, "r") as file:
        for line in file:
            id, task, status = line.strip().split("|")
            tasks.append({
                "id": int(id),
                "task": task,
                "status": status
            })

    for t in tasks:
        if t["id"] == task_id:
            found = True

            print("\n1. Update Task Title")
            print("2. Update Status")
            option = input("Choose option: ")

            if option == "1":
                new_task = input("New task title: ").strip()
                if new_task == "":
                    print("Empty value not allowed!")
                    return
                t["task"] = new_task

            elif option == "2":
                print("1. Pending")
                print("2. Completed")
                status_option = input("Choose: ")

                if status_option == "1":
                    t["status"] = "Pending"
                elif status_option == "2":
                    t["status"] = "Completed"
                else:
                    print("Invalid status!")
                    return
            else:
                print("Invalid option!")
                return

            break

    if not found:
        print("Task ID not found!")
        return

    with open(file_path, "w") as file:
        for t in tasks:
            file.write(f"{t['id']}|{t['task']}|{t['status']}\n")

    print("✅ Task updated successfully!")
    footer()


def delete_task():
    view_task()

    task_id = input("Enter Task ID to delete: ")

    if not task_id.isdigit():
        print("Invalid ID!")
        return

    task_id = int(task_id)

    tasks = []

    with open(file_path, "r") as file:
        for line in file:
            id, task, status = line.strip().split("|")
            if int(id) != task_id:
                tasks.append(line)

    with open(file_path, "w") as file:
        for line in tasks:
            file.write(line)

    print("✅ Task deleted successfully!")
    footer()


def main():
    print("\n------ Task Manager ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Selection: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
        footer()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid input!")
        main()


if __name__ == "__main__":
    main()
