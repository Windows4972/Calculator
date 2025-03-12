import math
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an opeation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")
operation = input()

if operation == "1": # PERFORM ADDITION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": # PERFORM SUBTRACT
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3": # PERFORM MULTIPLY
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4": # PERFORM DIVIDE
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5": # PERFORM SQUARE ROOT
    num = int(input("Enter number: "))
    print("The squareroot is %f " %(math.sqrt(num)) )
elif operation == "6": # SQUARE A NUMBER
    num = int(input("Enter number: "))
    print("The result is %d " %(pow(num, 2 )))
else:
    print("Invalid Entry")