# made by Ravelyk

import random
import pyperclip

def cringeifier(inString):
    if bool(random.getrandbits(1)):
        outputString = "> "
    else:
        outputString = ""

    for char in inString:
        if char != " ":
            check = bool(random.getrandbits(1)) # changed this to True if you don't want a normal character in the output

            if bool(random.getrandbits(1)):
                customChar = "`" + char + "`"
            else:
                customChar = char

            usedChar = []

            while check:
                randInt = random.randint(0, 4)
                while randInt in usedChar:
                    randInt = random.randint(0, 4)
                else:
                    usedChar.append(randInt)

                match randInt:
                    case 0:
                        customChar = "*" + customChar + "*"
                    case 1:
                        customChar = "_" + customChar + "_"
                    case 2:
                        customChar = "**" + customChar + "**"
                    case 3:
                        customChar = "__" + customChar + "__"
                    case 4:
                        customChar = "~~" + customChar + "~~"

                check = bool(random.getrandbits(1))

            outputString += customChar + chr(8202)
        else:
            outputString += "  "

    return outputString


inputString = input("Give the string boi: ")

pyperclip.copy(cringeifier(inputString))
pyperclip.paste()

print("You can now paste the cringe text")
