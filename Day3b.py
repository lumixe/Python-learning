
#To Create a simple ATM Login
u_name = input("Please enter your username: ")
pin = int(input("Please Enter your Secret number: "))
if u_name == "Olumide" and pin == 1234:
     print(f"Access Granted,Welcome {u_name} ")
else:
    print("Incorrect Username or Pin, Try again")
