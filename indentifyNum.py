# to identify target Number in a proper range. (liStart, liEnd)
def identNum(targetNum):
    number1 = input("Please select a number between 1 and 100:")
    while int(number1) < 1 or int(number1)>100:
        print("The number did NOT properly picked up.")
        number1 = input("Please select a number between 1 and 100:")
    print("The number is: " + number1)
    print("The number is ok.")             
    return(input)
identNum("Please input a number between 1 and 100:")
