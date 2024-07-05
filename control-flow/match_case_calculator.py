operation = input("Choose the operation (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Perform the calculation using Match Case  
match operation:  
case "+":
    result = num1 + num2
case "-":
   result = num1 - num2
case "*":
    result = num1 * num2
case "/":
    if num2 == 0:
    print("Cannot divide by zero.")
else:
    result = num1 / num2
    # Output the result  
if "result": 
    print(f"The result is [result]")  

