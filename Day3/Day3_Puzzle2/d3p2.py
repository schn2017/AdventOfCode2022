import sys
def main():
    inputFile = open(sys.argv[1], "r")

    prioritySum = 0
    group = []

    for line in inputFile:
        group.append(line.replace("\n", ""))

        if len(group) == 3:
            elf1Rucksack = set(group[0])

            for item in elf1Rucksack:
                # group[1] and group[2] represent the other two elves in the group of 3
                if item in group[1] and item in group[2]:
                    prioritySum += getItemPriority(item)
                    break

            # clear group when finished
            group.clear()

    inputFile.close()
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