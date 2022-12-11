def main():
    inputFile = open("input.txt", "r")

    maxCaloriesArr = [0, 0, 0]
    currentElfCalories = 0

    for line in inputFile:
        if len(line.strip()) == 0:
            if currentElfCalories >= maxCaloriesArr[2]:
                index = getIndex(maxCaloriesArr, currentElfCalories)

                # Shift contents of array over, should use deque instead
                if index == 0:
                    tmp = maxCaloriesArr[1]
                    maxCaloriesArr[2] = tmp
                    maxCaloriesArr[1] = maxCaloriesArr[0]
                    maxCaloriesArr[0] = currentElfCalories
                elif index == 1:
                    maxCaloriesArr[2] = maxCaloriesArr[1]
                    maxCaloriesArr[1] = currentElfCalories
                elif index == 2:
                    maxCaloriesArr[2] = currentElfCalories

            # Reset calories for next elf 
            currentElfCalories = 0
        else:
            currentElfCalories += int(line)

    print(maxCaloriesArr)
    print(sum(maxCaloriesArr))
    inputFile.close()

def getIndex(array, value):
    if value >= array[0]:
        return 0
    elif value >= array[1]:
        return 1
    else:
        return 2

if __name__ == "__main__":
    main()