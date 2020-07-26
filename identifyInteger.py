
number1 = input("Please input a integer number:")

while True:
    if number1.isdecimal():
        print("The number is good to go.")
        break
    else:
        print("Your input was not integer number, please enter int number.")
        number1 = input("Please input a good int number:")
print("Now the number is:" +number1)

