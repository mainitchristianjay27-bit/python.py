import os
os.system("cls")

def withdrawal():
    balance = 5000

    while True:
        print("\n--- Simple Money Withdrawal System ---")
        print(f"Current Balance: {balance}")

        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            if amount > balance:
                print("Insufficient funds!")
                print("Options: ")
                print("1. Exit")
                print("2. Check Balance")
                print("3. Try Again")

                choice = input("Choose an option (1/2/3): ")

                if choice == "1":
                    print("Exiting.....")
                    break
                elif choice == "2":
                    print(f"Your current balance is: {balance}")
                elif choice == "3":
                    continue
                else:
                    print("Invalid choice. Returning to main menu.")
            else:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: {balance}")

        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

withdrawal()
