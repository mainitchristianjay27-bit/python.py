import os
os.system("cls")
list = []

print("-- User management system --\n")
print("Good day, User! Enter a number.")



while True:

    print("1. Show Users\n2. Add User\n3. Update User\n4. Delete User\n5. Exit.")
    User = input("Enter a number: ")


    match User:
        case '1':
            print(list)
        case '2':
          print("-- ADD USER --")

          name = input("Enter a username: ")
          list.append(name)
        case '3':
            print("-- UPDATE USER --")
            old_name = input("Enter username to update: ")
            if old_name in list:
                new_name = input("Enter new username: ")
                index = list.index(old_name)
                list[index] = new_name
                print("User updated.")
            else:
                print("User not found.")
            input("\nPRESS ENTER TO CONTINUE....")
        case '4':
            print("-- DELETE A USERNAME --")
            name = input("Enter a username to delete: ")
            if name in list:
                list.remove(name)
                print("User deleted.")
            else:
                print("User not found.")
                print("Enter an existing username. Press enter to continue.")
        case '5':
            print("Exiting......")
            break
        case _:
            print("PAG TARONG UG BUTANG!")





