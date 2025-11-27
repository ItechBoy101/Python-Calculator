def add(n1,n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1,n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiply(n1,n2):
    """Returns the product of two numbers."""
    return n1 * n2
    
def divide(n1,n2):
    """Return the divded product."""
    if n2 == 0:
        return "Error!! Can't divide a value by zero"
    return n1/n2

#Main calculator logic with a loop for continuous calculating
def calculator():
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid choice.")

# Call the function to start the calculator
calculator()