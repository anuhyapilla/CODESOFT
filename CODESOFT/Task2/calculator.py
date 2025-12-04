def calculator():
    print("------ Simple Calculator ------")
    
    # Taking user input safely
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return

    print("\nChoose an operation:")
    print(" +  for Addition")
    print(" -  for Subtraction")
    print(" *  for Multiplication")
    print(" /  for Division")
    print(" %  for Modulus")
    print(" ** for Power")

    operation = input("Enter operation: ").strip()
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: "❌ Cannot divide by zero!" if b == 0 else a / b,
        "%": lambda a, b: "❌ Cannot modulus by zero!" if b == 0 else a % b,
        "**": lambda a, b: a ** b,
    }
    result = operations.get(operation)

    if result:
        print("\nResult:", result(num1, num2))
    else:
        print("❌ Invalid operation! Please choose a valid operator.")

    print("-------------------------------")
calculator()
