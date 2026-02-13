while True:
    password = input("Enter a number & letter: ")
    has_letter = False
    has_number = False

    for i in password: 
        if i.isalpha():
            has_letter = True

        if i.isdigit():
            has_number = True

    if  has_letter and has_number:
        print("Password accepted.")
        break
    else:
        print("Invalid password. Try again.")   