import os
os.system("cls")

try:
    with open("message.txt", "x") as file:
        print("File created successfully")

except:
    print("Error. File already exist!")

while True:
    print("--- REPLICA SA MESSENGER ---\n\n")
    print("Menu:")
    print("1. Exit the program")
    print("2. View all messages")
    print("3. Send a message")

    choice = int(input("Enter a choice: "))

    if choice == 1:
            print("Exiting....")
            break
    elif choice == 2:
            print("All messages: ")
            try: 
                with open("message.txt", "r") as file:
                    print(file.read())
            except:
                    print("No messages.")
            input("\nPress Enter. Return to menu!")
    elif choice == 3:
        new_message = input("Enter your message boi: ")
        with open("message.txt", "a") as file:
            file.write(new_message + "\n")
            print("Your message sent!")
        input("Press enter to return to menu.")
    else:
        print("Invalid choice!")