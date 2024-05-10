import math

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function does exponents
def exponent(x, y):
    return x ** y

# This function does roots
def root(x, y):
    return x ** (1/y)

# This function does logs
def log(x, y=None):
    if y is None:
        return math.log(x)
    else:
        return math.log(x, y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponential")
print("6.Root")
print("7.Logs")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter first number: "))
            if choice != '7':  # If the choice is not logarithm, ask for num2
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '7':
            # Prompt for the base input
            base_input = input("Enter base (or leave blank for Euler's number): ")
            # Set base to Euler's number if input is blank or consists only of whitespace characters
            if base_input.strip() == "":
                b = math.e
            else:
                try:
                    b = float(base_input)
                except ValueError:
                    print("Invalid input for base. Please enter a valid number.")
                    continue

            # Calculate and print the logarithm
            if num1 <= 0 or b <= 0 or b == 1:
                print("Error! Invalid input for logarithm.")
            else:
                print('Log({0}) {1} is {2}'.format(b, num1, log(num1, b)))
        else:
            # Perform other operations based on the user's choice
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
            elif choice == '5':
                print(num1, "^", num2, "=", exponent(num1, num2))    
            elif choice == '6':     
                if num2 <= 0:
                    print("Error! Cannot calculate the root with a non-positive number.")
                else:
                    print(num1, "√", num2, "=", root(num1, num2))
                    
        
        # check if user wants another calculation
        while True:
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == "yes":
                break
            elif next_calculation.lower() == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid Input")

#made by yrll0w