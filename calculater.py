def calculator():
    print("Simple Calculator")
    
    # Step 1: Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Step 2: Choose operation
    print("Choose operation: +, -, *, /")
    op = input("Enter operation: ")
    
    # Step 3: Perform calculation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"
    
    # Step 4: Display result
    return f"Result: {result}"


# Run the calculator
print(calculator())
