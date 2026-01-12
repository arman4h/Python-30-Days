file_path = "Contacts.txt"

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
        

def add_contacts():
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")
    
    contact = {
        "name" : name , 
        "email" : email,
        "phone" : phone
    }
    
    with open(file_path, 'a') as file:
        file.write(f"{contact['name']},{contact['email']},{contact['phone']}\n")

    print("Contact Added Successfully!.....")
    footer()
    
    
    
def view_contacts():
    print("#### All Save Contacts ####")
    print("Name        -----        Email        -----        Phone")

    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()

    print("\nEnd of the Contacts")
    footer()
    
def search_contact(key):
    key = key.lower()
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            name, email, phone = line.strip().split(",")
            if key in name.lower() or key in email.lower():
                print("\n Contact Found: ")
                print("Name: ", name)
                print("Email:", email)
                print("Phone:", phone)
                print("-" * 30)
                footer()
                break 
            else:
                line = file.readline()
        else :
            print("No Contact Found!")
    
    
def main():
    print("------Welcome to the Contact Directory------\n")
    print("Choose Option: \n")
    print("1.Add Contacts")
    print("2.View All Contacts")
    print("3.Search Contacts")
    print("4.Exit")
    print("\n")
    
    userinput = input("Selection: ")
 
    if userinput == "1" :
        add_contacts()
    elif userinput == "2":
        view_contacts()
    elif userinput == "3" :
        key = input("Enter Name or Email Here: ")
        search_contact(key)
    elif userinput == "4" :
        print("Have a good day ! ")
        return 0 
    else :
        print("Invalid Input ! Try Again...\n")
        main()
    
    

if __name__ == "__main__":
    main()
    