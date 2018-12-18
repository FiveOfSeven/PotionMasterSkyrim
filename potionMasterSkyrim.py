print ("Skyrim Potion Master Program\n")

#potionFile = open('./skyrimEffectsToIngredients', 'r')
#potionFile.close()

affectsListList = [[]]
lIsEmpty = 2
index = 0
usedIngredients = []
userInput = "empty"
ing1 = "empty"
ing2 = "empty"
ing3 = "empty"
ingredientCounter = 0
effectCount = 0
ingredientCounter2 = 0
effectCount2 = 0

with open('./skyrimEffectsToIngredients', 'r') as potionFile:
    for line in potionFile:
        if lIsEmpty == -1:
            lIsEmpty = 3
            garbage = line
        elif lIsEmpty == 2:
            affectsListList[index].append(line)
            lIsEmpty = 1
        elif lIsEmpty > 0:
            lIsEmpty -= 1
        elif lIsEmpty == 0:
            affectsListList[index].append(line)
        else:
            print ("error\n")
        if line in ['\n', '\r\n']:
            lIsEmpty = -1
            index += 1
            affectsListList.append([])
            #print (index)

print (affectsListList[0][0], end='')
print (affectsListList[0][1], end='')
print (affectsListList[0][2], end='')
print (affectsListList[0][3], end='')
for x in affectsListList[0]:
    print (x)


print ("press q to quit, d to display, n for next clock cycle")
userInput = input()
while userInput != 'q':
    if userInput == 'd':
        print ("ing1: ", ing1);
        print ("ing2: ", ing2);
        print ("ing3: ", ing3);
        print ("effectCount: ", effectCount);
        print ("ingredientCounter: ", ingredientCounter);
        print ("effectCount2: ", effectCount2);
        print ("ingredientCounter2: ", ingredientCounter2);
    elif userInput == 'n':
        if ing1 == "empty" and ing2 == "empty" and ing3 == "empty":
            if ingredientCounter == len(affectsListList[ingredientCounter]):
                ingredientCounter = 0
                effectCount += 1
                print ("do you have the ingredient %s (y or n)" % affectsListList[effectCount][ingredientCounter])
                haveIng = input()
                if haveIng == 'y':
                    ing1 = affectsListList[effectCount][ingredientCounter]
            else:
                ingredientCounter += 1
                print ("do you have the ingredient %s (y or n)" % affectsListList[effectCount][ingredientCounter])
                haveIng = input()
                if haveIng == 'y':
                    ing1 = affectsListList[effectCount][ingredientCounter]
        elif ing1 != "empty" and ing2 != "empty" and ing3 != "empty":
            print ("ing1: ", ing1);
            print ("ing2: ", ing2);
            print ("ing3: ", ing3);
            print ("ingredients are full, which ingredient is now empty (1, 2, or 3)")
        else:
            ingCount = 0
            if ing1 != "empty":
                ingCount += 1
            if ing2 != "empty":
                ingCount += 1
            if ing3 != "empty":
                ingCount += 1
            if ingCount == 1:
                print (ingredientCounter)
                print (affectsListList[ingredientCounter])
                if ingredientCounter == len(affectsListList[ingredientCounter]):
                    ingredientCounter = 0
                    effectCount += 1
                    ing1, ing2, ing3 = "empty"
                    print ("do you have the ingredient %s (y or n)" % affectsListList[effectCount][ingredientCounter2])
                    haveIng = input()
                    if haveIng == 'y':
                        ing1 = affectsListList[effectCount][ingredientCounter]
                else:
                    if ingredientCounter2 < ingredientCounter:
                        ingredientCounter2 = ingredientCounter
                    ingredientCounter2 = ingredientCounter2 + 1
                    print ("do you have the ingredient %s (y or n)" % affectsListList[effectCount][ingredientCounter2])
                    haveIng = input()
                    if haveIng == 'y':
                        ing2 = affectsListList[effectCount][ingredientCounter]



    print ("press q to quit, d to display, n for next clock cycle")
    userInput = input()
    
