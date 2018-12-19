print ("Skyrim Potion Master Program\n")

#potionFile = open('./skyrimEffectsToIngredients', 'r')
#potionFile.close()

def printMenu():
    print ("press q to quit, d to display, n for next clock cycle, s to dislpay a list, f to display an ingredient")


effectsListList = [[]]
lIsEmpty = 2
index = 0
usedIngredients = []
userInput = "empty"
ing1 = "empty"
ing2 = "empty"
ing3 = "empty"
ingredientCounter = 1
effectCount = 0
ingredientCounter2 = 1
effectCount2 = 0


with open('./skyrimEffectsToIngredients', 'r') as potionFile:
    for line in potionFile:
        if lIsEmpty == -1:
            lIsEmpty = 3
            garbage = line
        elif lIsEmpty == 2:
            effectsListList[index].append(line)
            lIsEmpty = 1
        elif lIsEmpty > 0:
            lIsEmpty -= 1
        elif lIsEmpty == 0:
            effectsListList[index].append(line)
        else:
            print ("error\n")
        if line in ['\n', '\r\n']:
            lIsEmpty = -1
            index += 1
            effectsListList.append([])
            #print (index)

print (effectsListList[0][0], end='')
print (effectsListList[0][1], end='')
print (effectsListList[0][2], end='')
print (effectsListList[0][3], end='')
for x in effectsListList[0]:
    print (x)

printMenu()
userInput = input()
while userInput != 'q':
    if userInput == 'f':
        print("Please input a list index")
        listIndex = input() 
        print("Please input an ingredient index")
        ingIndex = input()
        print (effectsListList[int(listIndex)][int(ingIndex)])
    if userInput == 's':
        print("Please input a list index")
        listIndex = input() 
        for x in effectsListList[int(listIndex)]:
            print (x)
    if userInput == 'd':
        print ("ing1: ", ing1);
        print ("ing2: ", ing2);
        print ("ing3: ", ing3);
        print ("effectCount: ", effectCount);
        print ("ingredientCounter: ", ingredientCounter);
        print ("effectCount2: ", effectCount2);
        print ("ingredientCounter2: ", ingredientCounter2);
        print ("usedIngredients: ", usedIngredients);
    elif userInput == 'n':
        if ing1 == "empty" and ing2 == "empty" and ing3 == "empty":
            while effectsListList[effectCount][ingredientCounter] in usedIngredients or ingredientCounter == len(effectsListList[effectCount]):
                ingredientCounter += 1
            if ingredientCounter == (len(effectsListList[effectCount]) - 1):
                print ("reached the end of list %s" % effectCount)
                ingredientCounter = 0
                effectCount += 1
                ingredientCounter2 = ingredientCounter
                effectCount2 = effectCount
            else:
                print ("do you have the ingredient %s (y or n)" % effectsListList[effectCount][ingredientCounter])
                haveIng = input()
                if haveIng == 'y':
                    ing1 = effectsListList[effectCount][ingredientCounter]
                if haveIng == 'n':
                    usedIngredients.append(effectsListList[effectCount][ingredientCounter])
                ingredientCounter += 1
                ingredientCounter2 = ingredientCounter
        elif ing1 != "empty" and ing2 != "empty" and ing3 != "empty":
            print ("ing1: ", ing1);
            print ("ing2: ", ing2);
            print ("ing3: ", ing3);
            print ("ingredients are full, which ingredient is now empty (1, 2, or 3)")
            print ("pay no attention to the previous line")
            ingredientCounter = 1
            ingredientCounter2 = 1
            effectCount2 = effectCount
            ing1 = "empty"
            ing2 = "empty"
            ing3 = "empty"
        else:
            ingCount = 0
            if ing1 != "empty":
                ingCount += 1
            if ing2 != "empty":
                ingCount += 1
            if ing3 != "empty":
                ingCount += 1
            if ingCount == 1:
                while effectsListList[effectCount][ingredientCounter2] in usedIngredients and ingredientCounter2 != len(effectsListList[effectCount]):
                    ingredientCounter += 1
                if ingredientCounter2 == (len(effectsListList[effectCount]) - 1):
                    print ("reached the end of list %s" % effectCount)
                    ingredientCounter = 0
                    effectCount += 1
                    ingredientCounter2 = ingredientCounter
                    effectCount2 = effectCount
                    ing1 = "empty"
                    ing2 = "empty"
                    ing3 = "empty"
                else:
                    print ("do you have the ingredient %s (y or n)" % effectsListList[effectCount][ingredientCounter2])
                    haveIng = input()
                    if haveIng == 'y':
                        ing2 = effectsListList[effectCount][ingredientCounter2]
                    if haveIng == 'n':
                        usedIngredients.append(effectsListList[effectCount][ingredientCounter2])
                    ingredientCounter2 = ingredientCounter2 + 1
            if ingCount == 2:
                print("ingcount2")
                matchExists = False
                for x in effectsListList[effectCount2]:
                    if x == ing1 or x == ing2:
                        matchExists = True
                while matchExists == False or effectCount2 >= len(effectsListList):
                    effectCount2 += 1
                    ingredientCounter2 = 0
                    for x in effectsListList[effectCount2]:
                        if x == ing1 or x == ing2:
                            matchExists = True
                if (effectCount2 >= len(effectsListList)):
                    print("reached the end of the the lists")
                    ing1 = "empty"
                    ing2 = "empty"
                    ing3 = "empty"
                else:
                    while effectsListList[effectCount2][ingredientCounter2] in usedIngredients and ingredientCounter2 != len(effectsListList[effectCount2]):
                        ingredientCounter += 1
                    if (effectCount == effectCount2):
                        print ("effectCounts are the same")
                        print ("reached the end of 2 list %s" % effectCount2)
                        effectCount2 += 1
                        ingredientCounter2 = 0
                    elif ingredientCounter2 == (len(effectsListList[effectCount2]) - 1):
                        print ("end of new effect list")
                        print ("reached the end of 2 list %s" % effectCount2)
                        ingredientCounter2 = 0
                        effectCount2 += 1
                    else:
                        print("incrementing 2 list")
                        if effectsListList[effectCount2][ingredientCounter2] == ing1 or effectsListList[effectCount2][ingredientCounter2] == ing2:
                            print ("there was a copy ingredient")
                            ingredientCounter2 += 1
                            if effectsListList[effectCount2][ingredientCounter2] == ing1 or effectsListList[effectCount2][ingredientCounter2] == ing2:
                                print ("there was a second copy ingredient")
                            else:
                                print ("do you have the ingredient %s (y or n)" % effectsListList[effectCount2][ingredientCounter2])
                                haveIng = input()
                                if haveIng == 'y':
                                    ing3 = effectsListList[effectCount2][ingredientCounter2]
                                if haveIng == 'n':
                                    usedIngredients.append(effectsListList[effectCount2][ingredientCounter2])
                        else:
                            print ("do you have the ingredient %s (y or n)" % effectsListList[effectCount2][ingredientCounter2])
                            haveIng = input()
                            if haveIng == 'y':
                                ing3 = effectsListList[effectCount2][ingredientCounter2]
                            if haveIng == 'n':
                                usedIngredients.append(effectsListList[effectCount2][ingredientCounter2])
                        if(len(effectsListList[effectCount2]) > ingredientCounter2):
                            ingredientCounter2 += 1
                        else:
                            ingredientCounter2 = 1
                            effectCount2 = 1

    printMenu()
    userInput = input()
    
