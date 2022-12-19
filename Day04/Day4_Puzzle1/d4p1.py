import sys
def main():
    inputFile = open(sys.argv[1], "r")

    fullyContainedPairs = 0

    for line in inputFile:
        pairs = line.replace("\n", "").split(",")
        pair1 = pairs[0].split('-')
        pair1Lower = int(pair1[0])
        pair1Upper = int(pair1[1])

        pair2 = pairs[1].split('-')
        pair2Lower = int(pair2[0])
        pair2Upper = int(pair2[1])

        if pair1Lower <= pair2Lower and pair1Upper >= pair2Upper:
            fullyContainedPairs += 1
        elif pair1Lower >= pair2Lower and pair1Upper <= pair2Upper:
            fullyContainedPairs += 1
    
    inputFile.close() 
    print("There are " + str(fullyContainedPairs) + " fully contained pairs.")

if __name__ == "__main__":
    main()