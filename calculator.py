def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Take user input for the operation
            choice = input("\nEnter your choice (1/2/3/4 or 'q' to quit): ").lower()

            # Exit the program
            if choice == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select a valid operation!")
                continue

            # Take user input for the numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
        except ValueError:
            print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    calculator()