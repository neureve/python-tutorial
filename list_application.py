def display_menu():
    print("\n--- to do list application ---")
    print("1. add a task")
    print("2. view all tasks")
    print("3. mark a task as a done")
    print("4. delete a task")
    print("5. exit")
    choice = input("Enter your choice: ")
    return choice

def add_task(tasks):
    task = input("enter the task you want to add: ")
    tasks.append(task)
    print("task", task, "added!")

def view_tasks(tasks):
    if tasks:
        print("\n your to do list:")
        for index, task in enumerate(tasks, 1):
            print(index,".", task)
    else:
        print("empty to do list!")
        
def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nenter the number of task you completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1] + " *"
            print("task", tasks[task_num - 1], "marked as done")
        else:
            print("invalid task number!")
    

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nenter the number pf task you want to delete: "))
        if 1 <= task_num <= len(tasks):
            delete_task = tasks.pop(task_num - 1)
            print("task", delete_task, "deleted")
        else:
            print("invalid task number")

def main():
    task = []
    while True:
        choice = display_menu()

        if choice == '1':
            add_task(task)
        elif choice == '2':
            view_tasks(task)
        elif choice == '3':
            mark_done(task)
        elif choice == '4':
            delete_task(task)
        elif choice == '5':
            print("good bye")
            break
        else:
            print("invalid choice! please select valid option!")
if __name__ == "__main__":
    main()



    



            



    