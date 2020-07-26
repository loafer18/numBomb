import random

numList = list(range(1,101))
#print (numList)
numBomb = random.choice(numList)
print(numBomb)
while True:
    try:
        #num= float(input("input a number pls."))
        number1 = input("Please select a number between 1 and 100:")
        number1 = int(number1)
        print(number1)        
        if number1 == numBomb:
            print("Congratulations, you picked the BOMB! YOU LOOSE!!!")
        elif number1 < numBomb:
            #print("input number is positive")
            numList = list(range(number1,101))
            print(numList)
        else:
            #print("input number is negative")
            numList = list(range(1,number1))
            print (numList)
        break
    except ValueError:
        print("input is invalid, please reenter.")
