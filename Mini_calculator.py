def calculate(operation, num1, num2):
    if operation.lower() == "add":
     print(int(num1 + num2))
    elif operation.lower() == "subtract":
     print(int(num1 - num2))
    elif operation.lower() == "multiply":
     print(int(num1 * num2))
    elif operation.lower() == "divide":
     print(int(num1 / num2))

calculate("add", 2, 5)
calculate("subtract", 10, 3)
calculate("multiply", 2, 4)
calculate("divide", 10, 2)

        
    
  


