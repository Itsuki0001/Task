Task_List = []
Pending_Task = []
completed_task = []
num_of_task = 0


def add_task():
    global num_of_task
    user_input = str(input("Enter Task: "))
    Task_List.append(user_input)
    Pending_Task.append(user_input)
    num_of_task += 1


def complete_task():
    print(Pending_Task)
    user_input = str(input("Choose The Following Task You Have Done: "))
    Pending_Task.remove(user_input)
    completed_task.append(user_input)
    print(f"You have completed {completed_task} task")


def delete_task():
    user_input = input("Are you sure you want to delete the task? (y/n): ")
    while True:
        match user_input:
            case "y":
                print(Task_List)
                user_input = str(input("Enter Task: "))
                Task_List.remove(user_input)
            case "n":
                break
            case _:
                break

def show_task():
    print(f"Your task list is {Task_List}")
    print(f"Pending task are {Pending_Task}")
    print(f"Completed task are {completed_task}")


def main():
    while True:
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Show Task")
        print("5. Exit")
        user_input = int(input("Enter Your Choice: "))
        match user_input:
            case 1:
                add_task()
            case 2:
                complete_task()
            case 3:
                delete_task()
            case 4:
                show_task()
            case 5:
                print("Thank You For Using This App")
                break
            case _:
                print("Invalid Input")

if __name__ == '__main__':
    main()