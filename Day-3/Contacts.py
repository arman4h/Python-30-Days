file_path = "./Contacts.txt"

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
        file.write(f"{contact['name']}, {contact['email']}, {contact['phone']}\n")

    print("Contact Added Successfully!.....")
    
def main():
    print("This is the main function")
    add_contacts()

if __name__ == "__main__":
    main()
    