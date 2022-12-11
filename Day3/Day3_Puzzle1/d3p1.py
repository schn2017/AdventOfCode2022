import sys

def main():
    rucksacks = open(sys.argv[1], "r")
    prioritySum = 0

    for rucksack in rucksacks:
        compartment1 = rucksack[slice(0, len(rucksack)//2)]
        compartment2 = rucksack[slice(len(rucksack)//2, len(rucksack))]

        uniqueItemsInCompartment1 = set(compartment1)
        
        for item in uniqueItemsInCompartment1:
            if item in compartment2:
                prioritySum += getItemPriority(item)
                break

    rucksacks.close()
    print("The priority sum is " + str(prioritySum))

def getItemPriority(itemCharacter):
    itemPriority = 0

    if itemCharacter.isupper():
        # -64 for ascii conversion + 25 because values A - Z is 27 - 52 in priority
        itemPriority = ord(itemCharacter) - 64 + 26
    elif itemCharacter.islower():
        itemPriority = ord(itemCharacter) - 96

    return itemPriority

if __name__ == "__main__":
    main()