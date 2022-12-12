import sys
def main():
    inputFile = open(sys.argv[1], "r")
    overlappingPairs = 0

    for line in inputFile:
        pairs = line.replace("\n", "").split(",")
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')

        if doPairsOverLap(pair1, pair2):
            overlappingPairs += 1
        elif doPairsOverLap(pair2, pair1):
            overlappingPairs += 1

    print("There are " + str(overlappingPairs) + " overlapping contained pairs.")

def doPairsOverLap(pair1, pair2):
    pair1Lower = int(pair1[0])
    pair1Upper = int(pair1[1])
    pair2Lower = int(pair2[0])
    pair2Upper = int(pair2[1])

    return (pair1Lower <= pair2Lower and pair2Lower <= pair1Upper) or (pair1Lower <= pair2Upper and pair2Upper <= pair1Upper)


if __name__ == "__main__":
    main()