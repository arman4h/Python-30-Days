## Day 1 - CLI Calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b == 0:
        raise ValueError("Cannot Devided by Zero")
    
    return a/b

def showMenu():
    print("\n### Welcome to CLI Calculator ###")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

def getNummber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please Enter the valid error")

def saveHistory(record):
    with open("History.txt", "a") as file:
        file.write(record + "\n")

def main():
    while True:
        showMenu()
        choice = input("Enter your choice(1-5):  ")

        if choice == '5':
             print("Good bye ! Have a nais day")
             break

        if choice not in {'1','2','3','4'}:
            print('Invalid Input! ')
            continue

        a = getNummber("Enter the first number: ")
        b = getNummber("Enter the second number: ")

        try:
            if choice == '1':
                result = add(a,b)
                operation = f"{a} + {b} = {result}"

            elif choice == '2':
                result = sub(a,b)
                operation = f"{a} - {b} = {result}"

            elif choice == '3':
                result = multiply(a,b)
                operation = f"{a} * {b} = {result}"
            
            elif choice == '4':
                result = division(a,b)
                operation = f"{a} / {b} = {result}"

            print("The Result is : ", result)
            saveHistory(operation)

        except ValueError as e:
            print("Error", e) 
    

if __name__ == "__main__":
    main()
