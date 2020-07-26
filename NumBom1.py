# This game is based with a Sunday game with Lily and Mickey at 7/19/2020. That way really fun. Love~~~
# Game rule: 3 players, they pick one number one by one, each time compare with computer initial number, the last one 
# coding=utf-8
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
# Game ask for player 1 input number 1. 
number1 = input("Please select a number between 1 and 100:")
number1 = int(number1)
loop = 0
while number1 != numBomb:
    try:
        if number1 < numBomb:  # user number < bomb
            if loop < 1:
                liStart= number1
                liEnd = 101
                numList = list(range(liStart,liEnd))
                print("Now the new range is " +str(numList))
                number1 = input("Please select a number between %d and 100" %liStart +":")
                number1 = int(number1)
                loop +=1
            else:
                liStart = number1           
                numList = list(range(number1, liEnd+1))
                print("Now the new range is " + str(numList))
                number1 = input("Please select a number between " +str(number1) +" and " + str(liEnd) +":")
                number1 = int(number1)
                liStart = number1
                loop +=1
        else:  # user number > bomb 
            #print("input number is negative")
            if loop < 1:
                numList = list(range(1,number1+1))  
                liEnd = number1
                print ("Now the new range is " + str(numList))
                number1 = input("Please select a number between 1 and " + str(liEnd)+":")
                number1 = int(number1)
                loop +=1
            else:
                #liStart = 1
                numList = list(range(liStart, number1+1))
                liEnd = number1
                print ("Now the new range is " + str(numList))
                number1 = input("Please select a number between 1 and " + str(liEnd)+":")
                number1 = int(number1)
                loop +=1
    except ValueError:
        print("input invalid, please enter a number.")
print("Congratulations, you picked the BOMB! YOU LOOSE!!!")
