file_path = "task.txt"

def footer():
    print("\n")
    print("0.Main")
    print("1.Exit")
    myinput = input("Selection: ")
    
    if myinput == "0":
        main()
    elif myinput == "1":
        print("Have a good day ! ")
        return 0 
    else:
        print("Invalid Input Try Again: ")
        footer()

def add_task():
    name = input("Task Name: ")
    status = input("Status: ")
    count = 0
    
    with open(file_path, "r") as file:
        for line in file:
            count += 1 
    
    id = count + 1
    
    task = {
        "id" : id ,
        "task" : name , 
        "status" : status
    }
    
    with open(file_path,"a") as file:
        file.write(f"{task['id']}|{task['name']|{task['status']}}\n")
    
    
    print("Contact Added Successfully!.....")
    footer()
    
def view_task():
    print("##### All Listed Task ######")

    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()
    
    print("##### End of the list ######")
    footer()
    
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
        delete_task()
    elif userinput == "5" :
        print("Have a good day ! ")
        return 0 
    else :
        print("Invalid Input ! Try Again...\n")
        main()
    
    

if __name__ == "__main__":
    main()