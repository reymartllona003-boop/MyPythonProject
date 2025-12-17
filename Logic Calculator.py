print("Logic Calculator")

print("Select operation:")
print("1. AND")
print("2. OR ")
print("3. NOT")
print("4. NAND")
print("5. NOR")
print("6. Exit")

def InputNumber():
    a = input("Enter First Number (0 or 1): ")
    b = input("Enter Second Number (0 or 1): ")
    return a, b


while True:

    choice = input("Enter Operation (1/2/3/4/5/6): ")    

    if choice == "6":
        print("Exiting the Logic Calculator.")
        break

    if choice == "1":
        print("You selected AND operation.")
        a,b = InputNumber()
        print(f"The Value is:", "1" if a == "1" and b == "1" else "0")

    elif choice == "2":
        print("You selected OR operation.")
        a, b = InputNumber()
        print(f"The Value is:", "1" if a == "1" or b == "1" else "0")

    elif choice == "3":
        print("You selected NOT operation.")
        a = input("Enter Number (0 or 1): ")
        print(f"The Value is: ", "1" if a == "0" else "0")
    
    elif choice == "4":
        print("You selected NAND operation.")
        a, b = InputNumber()
        print(f"The Value is: ", "1" if a == "1" or b == "1" else "0")

    elif choice == "5":
        print("You selected NOR operation.")
        a, b = InputNumber()
        print(f"The Value is: ", "1" if a == "1" and b == "1"  else "0")