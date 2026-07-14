#This code is used to request for input of price and quantity and give you the total price.

p_apple = int(input("Enter the price of the apple: "))

q_apple = int(input("How many apples? "))

total = p_apple * q_apple

print(f"The total price is #{total:,}")
