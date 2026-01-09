
def get_number(value):
     while True:
          try:
               return input(float(value))
          except ValueError:
               print("Invalid value Format! Try again")

def calculate_total(arr):
     leng = len(arr) 
     total = sum(arr) 
     calculate_avarage(total,leng)


def calculate_avarage(total,leng):
     avarage = total/leng 
     print_result(avarage)


def print_result(average):
    if average < 0:
        print('Student has a problem! Take some help.')
    elif 0 <= average < 56:
        print('Your Average Grade: D')
    elif 56 <= average < 72:
        print('Your Average Grade: C')
    elif 72 <= average < 80:
        print('Your Average Grade: B')
    elif 80 <= average < 90:
        print('Your Average Grade: A-')
    elif 90 <= average <= 100:
        print('Your Average Grade: A+')
    else:
        print("You are over genius!")  


def main():
    print("#######----Check Your Result Grading---#######")

    print('Enter You Marks by using spaces in this order !\n')
    print("Math English Physics Chemistry CSE")
    
    arr = list(map(int, input().split()))
    if len(arr) != 5:
        print("Please enter exactly 5 marks!")
        return

    calculate_total(arr)


if __name__ == "__main__":
     main()