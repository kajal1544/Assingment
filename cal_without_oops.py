# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
number_1 = 8
number_2 = 2

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            print(number_1, "+",number_2, "=", add(number_1, number_2))

        elif choice == '2':
            print(number_1, "-", number_2, "=", subtract(number_1,number_2))

        elif choice == '3':
            print(number_1, "*",number_2, "=", multiply(number_1,number_2))

        elif choice == '4':
            print(number_1, "/",number_2, "=", divide(number_1,number_2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")