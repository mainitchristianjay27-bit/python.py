import os
os.system("cls")

while True:
    print("--- ANG DIARY NG PANGET ---\n")
    print("1. Create")
    print("2. Append")
    print("3. Read")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter numbers only")
        continue
    match choice:
        case 1:
            try:
                filename = input("Enter the filename (example: test.txt): ")
                with open(filename, "x") as file:
                    texts = input("Write contents: ")
                    file.write(texts)
                print("File Created successfully")
            except:
                print("File already exists")
        case 2:
            try:
                filename = input("Enter the filename you want to append to: ")
                if not os.path.exists(filename):
                    print("ANG FILE DOL DILI GA EXIST. PLEASE HIMO SAG FILE UNA.")
                else:
                    with open(filename, "a") as file:
                        contents = input("Write contents: ")
                        file.write(contents)
                    print("Added contents successfully!")
            except:
                print("DILI GA EXIST ANG FILE OY...")
        case 3:
                try:
                    filename = input("Enter the filename to read: ")
                    if not os.path.exists(filename):
                        print("File does not exist.")
                    else:
                        with open(filename, "r") as file:
                            contents = file.read()
                            print("\n" + contents)
                except:
                    print("File already exists.")
        case 4:
            try:
                filename = input("Enter the filename to update: ")
                if not os.path.exists(filename):
                    print("File does not exist.")
                else:
                    with open(filename, "r") as file:
                        old_contents = file.read()
                        print("- Current Contents -")
                        print(old_contents)

                        new_contents = input("\nWrite new contents: ")
                        with open(filename, "w") as file:
                            file.write(new_contents)
                            print("File updated succesfully!")
            except:
                print("Error updating file.")
        case 5:
            try:
                filename = input("Enter the filename to delete: ")
                if os.path.exists(filename):
                    os.remove(filename)
                    print("File deleted.")
                else:
                    print("File does not exist.")
            except:
                print("Error deleting file.")
        case 6:
            print("Exiting....")
            break
        case _:
            print("Please choose 1-6.")
