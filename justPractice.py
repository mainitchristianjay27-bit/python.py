import os
os.system("cls")
psw = "qwertyuiopasdfghjklzxcvbnm"
attempts = 4

for i in range(attempts):
    user_input = input("Enter your password: ")
    if user_input == psw:
        print("Logged in.")
        break
    else:
        remaining = attempts - (i + 1)
    if remaining > 0:
        print("Incorrect password. Please try again.")
        print(f"Attempts remaining: {remaining}")
    else:
        print("Too many failed attempts. Access locked.")
        
