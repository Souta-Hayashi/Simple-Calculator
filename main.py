# Simple Calculator

# Add
def add(x, y):
    return x + y


# Subtract
def subtract(x, y):
    return x - y


# Multiply
def multiply(x, y):
    return x * y


# Divide
def divide(x, y):
    return x / y


print("Select option")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Choose option
while True:
    choice = input("Enter option(1 - 4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter digit: "))
        num2 = float(input("Enter digit: "))

        if choice == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))

        elif choice == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))

        elif choice == '3':
            print(num1, " × ", num2, " = ", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                raise Exception("Sorry, last number cannot be zero when dividing!")
            else:
                print(num1, " ÷ ", num2, " = ", divide(num1, num2))

        # Checking for another calculation
        another_calculation = input("Do you want another calculation?(yes/no): ")
        if another_calculation == "no":
            break

    elif type(choice) is str:
        raise Exception("Sorry! You only have 4 options: 1, 2, 3 and 4.")

    else:
        raise Exception("Sorry! You only have 4 options: 1, 2, 3 and 4.")
