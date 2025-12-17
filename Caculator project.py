print("Arithmetic Operation Calculator")

i = 1 

result = float(input("Enter 1 number: "))

while True:

    print("Choose Calculator")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. =")   

    choice = input("Input Calculator: ")

    if choice == "5":
        print("Final Result", result)
        break

    i += 1

    num = float(input(f"Enter {i} number:"))

    if choice == "1":
        def result_add(a, b):
            return a + b
        result = result_add(result, num)
    
    elif choice == "2":
        def result_subtract(a, b):
            return a - b
        result = result_subtract(result, num)
    elif choice == "3":
        def result_multiply(a, b):
            return a * b
        result = result_multiply(result, num)
    elif choice == "4":
        def result_divide(a, b):
            return a / b
        result = result_divide(result, num)
    else: 
        print("Invalid Choice")

    print("Current Result", result)