# This module contains functions
# for use in other scripts.

def printDivider():
    print("****************************")

def printMessage(message, includeNewLine):
    if includeNewLine:
        print(message)
    else:
        print(message, endline="")

def readInt(prompt):
    # keep prompting the user until they enter a valid int
    valid = False
    num = 0
    while valid == False:
        try:
            num = int(input(prompt))
            valid = True
        except:
            print("Please enter a valid integer")

    return num

def readString(prompt, canBeEmpty):
    valid = False
    while valid == False:
        string = input(prompt)
        string = string.strip()

        if string != "":
            valid = True
        elif string == "" and canBeEmpty == True:
            valid = True
        else:
            print("Enter a valid string")

