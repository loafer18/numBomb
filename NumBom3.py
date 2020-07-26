import random
# Score of each(later)
# Computer pick a random number between 1 and 100
# setup a number range from 1 to 100
numList = list(range(1,101))
#print (numList)
numBomb = random.choice(numList)
print (numBomb)
# Start main loop
# Player 1 choose number 1, computer feedback. if not the Bomb, player 2 action.
# program check user input and identify the number in proper range (liStart, liEnd) every time.
number1 = input("Please select a number between 1 and 100:")
number1 = int(number1)
while number1<1 or number1>100:
    print("The number did NOT properly picked up.")
    number1 = input("Please select a number between 1 and 100:")
    number1 = int(number1)
print("The number is: " + str(number1))
print("The number is ok.")             
loop = 0
while number1 != numBomb:
    try:
        if loop < 1:  # if the first time identify number
            if number1 < numBomb:  # user number < bomb
                liStart= number1
                liEnd = 101
                numList = list(range(liStart,liEnd))
                print("Now the new range is " +str(numList))
                liStart=numList[0]
                liEnd=numList[-1]
                number1 = input("Please select a number between %d and 100" %liStart +":")
                number1 = int(number1)
                while number1<liStart or number1>liEnd:
                    print("The number did NOT properly picked up.")
                    number1 = input("Please select a number between 1 and 100:")
                    number1 = int(number1)
                loop +=1
            else:  # user number > bomb
                liStart = 1
                liEnd= number1           
                numList = list(range(1, liEnd+1))
                print("Now the new range is " + str(numList))
                liStart=numList[0]
                liEnd=numList[-1]
                number1 = input("Please select a number between " +str(liStart) +" and " + str(liEnd) +":")
                number1 = int(number1)
                loop +=1
        else:  # loop >= 1
            if int(number1) < numBomb:  # user number < bomb
                liStart= int(number1)
                liEnd = numList[-1]
                numList = list(range(liStart,liEnd+1))
                print("Now the new range is " +str(numList))
                liStart=numList[0]
                liEnd=numList[-1]
                number1 = input("Please select a number between %r and %r" %(liStart,liEnd))
                while int(number1) >= liEnd or int(number1) <= liStart:
                     print("The number did NOT properly picked up.")
                     number1 = input("Please select a number between %r and %r:" %(liStart, liEnd))
                     number1 = int(number1)
                loop +=1
            else:  # user number > bomb
                liStart = numList[0]
                liEnd= int(number1)
                numList = list(range(liStart, liEnd+1))
                print("Now the new range is " + str(numList))
                liStart=numList[0]
                liEnd=numList[-1]
                number1 = input("Please select a number between " +str(liStart) +" and " + str(liEnd) +":")
                while int(number1) >= liEnd or int(number1) <= liStart:
                     print("The number did NOT properly picked up.")
                     number1 = input("Please select a number between %r and %r:" %(liStart, liEnd))
                     number1 = int(number1)
                loop +=1
    except ValueError:
        print("input invalid, please enter a number.")
print("Congratulations, you picked the BOMB! YOU LOOSE!!!")
