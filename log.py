import math

a_input = input('Number=')

b_input = input('Base=')

#default base is e
try:
    b = float(b_input)
except ValueError:
    b = math.e    

#convert to a to float
try:
    a = float(a_input)
except ValueError:
    print("Invalid input for number. Please enter a valid number")
    exit()            

output = math.log(a, b)

print('Log({0}) {1} is {2}'.format(b,a,output))