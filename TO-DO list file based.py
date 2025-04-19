todolist = [""]
running = True

def fileview():
    todo_file = open("todo_file.txt" , "r")
    if not todolist:
        print("no task in the list")
    else:
        print("\n todo list: ")
        for task in todolist:
            print(task)
            print(todo_file.read())
    todo_file.close()
def fileadd():
    todo_file = open("todo_file.txt" ,"a")
    task = input("enter your task")
    todo_file.write(task + "\n")  # <-- adds a new line after each task
    todo_file.close()
    print(f"Task '{task}' added successfully.")

# def addlist():
#     task = input("enter your task")
#     todolist.append(task)
#     print(f"task : {task} added successefully")

# def viewtask(todolist):
#     if not todolist:
#         print("no task in the list")
#     else:
#         print("\n todo list: ")
#         for task in todolist:
#             print(task)
#             print("\n")
def removetask():
    taskremove = input("Enter the task you want to remove: ").strip()

    f = open("todo_file.txt", "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        print("The file is empty.")
        return

    if taskremove + "\n" in lines:
        lines.remove(taskremove + "\n")
        f = open("todo_file.txt", "w")
        f.writelines(lines)
        f.close()
        print(f"'{taskremove}' removed successfully.")
    else:
        print("The task is not in the list.")

def switch(op):
    match op:
        case "add":
            # addlist()
            fileadd()
        case "view":
            # viewtask(todolist)
            fileview()
        case "remove":
            removetask()
        case _:
            print("Invalid choice! Please enter ADD, VIEW, or REMOVE.")
        

while running:
    op = input("\nChoose an action: [ADD] to add task, [VIEW] to view tasks, [REMOVE] to delete task\n").lower()
    switch(op)
    choice = input("to exit from the todo list (yes/no) ").strip().lower()
    if choice == "yes":
        running = False
        print("thank you for using the app!")

