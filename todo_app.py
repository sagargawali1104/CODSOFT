# To-Do List Project in Python
def show_menu():
    print("\n--- To-Do List MENU ---")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. DELETE TASK")
    print("4. EXIT")

def main():
    tasks = []  # list to store tasks

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added successfully!")

        elif choice == '2':
            if not tasks:
                print("No tasks in the List.")
            else:
                print("\n--- Your Tasks ---")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")

        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\n--- Your Tasks ---")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' deleted successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
 