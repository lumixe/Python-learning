users = {
    "admin": 1234,
    "olumide": 4321,
    "guest": 1111
}

balance = 50000


def check_balance(username):
    print(f"Your balance is ₦{balance}")

    with open("transactions.txt", "a") as file:
        file.write(f"{username} checked balance.\n")


def deposit(username):
    print("Deposit Successful")

    with open("transactions.txt", "a") as file:
        file.write(f"{username} deposited successfully.\n")


def withdraw(username):
    print("Withdrawal Successful")

    with open("transactions.txt", "a") as file:
        file.write(f"{username} withdrew successfully.\n")


def login():
    attempt = 0

    username = input("Enter your username: ")
    pin = int(input("Enter your PIN: "))

    while attempt < 3 and (username not in users or users[username] != pin):
        print("Incorrect Username or PIN")
        attempt += 1

        if attempt == 3:
            print("Account Blocked")
            return

        username = input("Enter your username: ")
        pin = int(input("Enter your PIN: "))

    print("Access Granted")

    with open("transactions.txt", "a") as file:
        file.write(f"User {username} logged in successfully.\n")

    while True:
        print(f"""
Welcome @{username}

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(username)

        elif choice == "2":
            deposit(username)

        elif choice == "3":
            withdraw(username)

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid option")
            
login()
