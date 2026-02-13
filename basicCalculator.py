result = ""
calculator = float(input("Enter your first number: "))
calculator2 = float(input("Enter your second number: "))

print("1. Multiplication")
print("2. Division")
print("3. Addition")
print("4. Subtraction")


choice = input("Enter your choice: ")

if choice == "1":
    print("Result:", calculator * calculator2)
    result = calculator * calculator2
    print("Result", int(result))
elif choice == "2":
    if calculator2 != 0:
        print("Result", calculator / calculator2)
    else: 
        print("Error: Division by zero is not allowed.")
elif choice == "3":
    print("Result:", calculator + calculator2)
    result = calculator + calculator2
    print("Result:" , int(result))
elif choice == "4":
    print("Result:", calculator - calculator2)
    result = calculator - calculator2
    print("Result:", int(result))
else:
    print("Error. Please enter the correct number!")            
    print("Error! Not in the choices.")           