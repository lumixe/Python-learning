#Simple ATM Pin

correct_pin = 1234
pin = int(input("Enter your pin: "))

while pin != correct_pin:
    print("incorrect pin, try again")
    pin = int(input("Enter your pin: "))

print("Access granted")
