# to do list

a=input("Enter your name : ")
print("Hello, " + a + "!")
to_do = []

def add_task():
    task = input("Enter a task: ")
    to_do.append(task)
    print(f"Task added: {task}")

def del_task():
    delt= int(input("Enter the no. you want to remove"))
    to_do.pop(delt-1)
    print("Task removed")

def view():
    print("Your tasks:")
    for i in range(len(to_do)):
        print(f"{i}. {to_do[i]}")
def tlist():
    do=int(input("Press associated key:\n 1.Add Task\n 2.Del Task\n 3.View your to-do list\n 4.Exit To-do list\n Enter your Choice: "))
    if do == 1:
        add_task()
        tlist()
    elif do == 2:
        del_task()
        tlist()
    elif do == 3:
        view()
        tlist()
    elif do == 4:
        print("Exiting to-do list")
        print("Bye Bye")
    else:
        print("Invalid choice")

tlist()
