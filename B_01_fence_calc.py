def num_check(question):
    error = "Invalid value\n"
    while True:

        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost per metre: ")

    perimeter = 2 * (width + length)
    price = perimeter * cost

    print()
    print(f"Perimeter: {perimeter}m")
    print(f"Price: ${price}")

    keep_going = input("Press enter to continue, or any other key to quit. ")
    print()

print("Thank you for using the fence calculator")
