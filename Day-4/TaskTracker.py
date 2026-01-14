file_path = "task.txt"

def add_task():
    print("Adding Task")
    
    
def view_task():
    print("View Task")
    
    
def update_task():
    print("Updating task")

def delete_task():
    print("Deleting task")






def main():
    print("------Welcome to the Task Manager ------\n")
    print("Choose Option: \n")
    print("1.Add Tasks")
    print("2.View All Tasks")
    print("3.Update existing tasks")
    print("4.Delete Tasks")
    print("5.Exit")
    print("\n")
    
    userinput = input("Selection: ")
 
    if userinput == "1" :
        add_task()
    elif userinput == "2":
        view_task()
    elif userinput == "3" :
        update_task()
    elif userinput == "4" :
        update_task()
    elif userinput == "5" :
        print("Have a good day ! ")
        return 0 
    else :
        print("Invalid Input ! Try Again...\n")
        main()
    
    
    
    
    

if __name__ == "__main__":
    main()