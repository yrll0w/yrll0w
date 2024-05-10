import math

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def sec(x):
    return 1 / cos(x)

def csc(x):
    return 1 / sin(x)

def cot(x):
    return 1 / tan(x)

def main():
    while True:
        print("Trigonometric Calculator")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Sec")
        print("5. Csc")
        print("6. Cot")
        choice = int(input("Enter your choice (1-6): "))
        angle = float(input("Enter the angle in degrees: "))
        
        if choice == 1:
            print("Sin({}) = {}".format(angle, sin(angle)))
        elif choice == 2:
            print("Cos({}) = {}".format(angle, cos(angle)))
        elif choice == 3:
            print("Tan({}) = {}".format(angle, tan(angle)))
        elif choice == 4:
            print("Sec({}) = {}".format(angle, sec(angle)))
        elif choice == 5:
            print("Csc({}) = {}".format(angle, csc(angle)))
        elif choice == 6:
            print("Cot({}) = {}".format(angle, cot(angle)))
        else:
            print("Invalid choice")
        
        while True:
            again = input("Do you want to calculate again? (yes/no): ").lower()
            if again == "yes":
                break
            elif again == "no":
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
