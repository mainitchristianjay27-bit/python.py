import os
os.system("cls")

def password_strength():
    letters = 26
    digits = 10

    total = (letters ** 2) * (digits ** 2)

    weak_letters = letters * (digits ** 2)   
    weak_digits = digits * (letters ** 2)    
    both_weak = letters * digits             

    weak = weak_letters + weak_digits - both_weak
    strong = total - weak
    print("Total possible passwords:", total)
    print("Weak passwords:", weak)
    print("Strong passwords:", strong)
password_strength()
