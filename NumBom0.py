import random
# Score of each(later)

# Computer pick a random number between 1 and 100
# setup a number range from 1 to 100
numList = list(range(1,101))
#print (numList)
numBomb = random.choice(numList)
#print (numBomb)

# Start main loop


# Player 1 choose number 1, computer feedback. if not the Bomb, player 2 action.
# Game ask for player 1 input number 1. 
while True:
	try:
                    number1 = input("Please select a number between 1 and 100:")
                    print(number1)
                    if number1 == numBomb:
                            print("Congratulations, you picked the BOMB! YOU LOOSE!!!")
                    elif number1 < numBomb:
                            numList = list(range(number1,101))
                    else:
                          #print("input number is negative")
                          numList = list(range(1,number1+1))
                          print (numList)
                    break
            except:
                    #print("input invalid, pls reenter again.")
