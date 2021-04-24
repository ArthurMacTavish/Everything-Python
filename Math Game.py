#Initial Program Command
import sys
import os
import random
titleCommand_UNIX = sys.stdout.write
titleCommand_MSWin = os.system

#Change Title
titleCommand_UNIX("\x1b]2;Math Game\x07")
titleCommand_MSWin("Math Game")

#Randomizer Mecha
    #Math Operation:
        # 1 = +
        # 2 = -
        # 3 = *
        # 4 = /
firstNumber = random.randint(1,50)
secondNumber = random.randint(1,50)
initialMathOperation = random.randint(1,4)

#Math Randomizer Mecha
if initialMathOperation == 1:
        mathOperationMark = " + "
        mathOperationCode = (firstNumber + secondNumber)
elif initialMathOperation == 2:
        mathOperationMark = " - "
        mathOperationCode = (firstNumber - secondNumber)
elif initialMathOperation == 3:
        mathOperationMark = " x "
        mathOperationCode = (firstNumber * secondNumber)
elif initialMathOperation == 4:
        mathOperationMark = " : "
        mathOperationCode = (firstNumber / secondNumber)

#User Input
print("What's your name?")
name = input("My name is ")

print("Hello, " + name + "!")
answer = int(input(str(firstNumber) + mathOperationMark + str(secondNumber) + " = "))

#Computing and Result

if answer == int(mathOperationCode):
    print("Ding! Ding! You're correct, " + name + "!")
    input("Press any key to Exit!")
else:
    print("Sorry, You're wrong, " + name + "!")
    input("Press any key to Exit!")