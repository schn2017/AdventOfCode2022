import sys

inputFile = open(sys.argv[1], "r")

maxCalories = 0
currentElfCalories = 0

for line in inputFile:

    if len(line.strip()) == 0:
        if currentElfCalories > maxCalories:
            maxCalories = currentElfCalories
        
        currentElfCalories = 0
    else:
        currentElfCalories += int(line)

print(maxCalories)
inputFile.close()