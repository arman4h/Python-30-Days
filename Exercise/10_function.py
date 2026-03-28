def caculate_area(height, base, choice = "1" ):
    match choice:
        case "1":
            area = ((1/2)*base*height) 
        case "2":
            area = (base*height) 
        case _:
            print("Invalid choice. Please select 1 or 2.")
            return
    print(area) 
    
def main():
    base = float(input("Enter Base: \n"))
    height = float(input("Enter Height: \n"))
    print("Enter your shape: \n")
    print("1.Triangle \n")
    print("2.Rectangle \n")

    shape = input("Your Choice: ") 
    caculate_area(height, base , shape)
    

if __name__ == "__main__":
    main()
    