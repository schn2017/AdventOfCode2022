import re

moveValues = {
    "A": 1,
    "B": 2,
    "C": 3
}

# A rock, B paper, C scissors
# X lose, Y draw, Z Win
rulesDict = {
    "AX": "C",
    "AY": "A",
    "AZ": "B",
    "BX": "A",
    "BY": "B",
    "BZ": "C",
    "CX": "B",
    "CY": "C",
    "CZ": "A"
}

inputFile = open("input.txt", "r")
finalScore = 0 

for line in inputFile:
    if (len(line.strip()) > 0):
        round = re.sub(r'\W+', '', line)


        yourMove = rulesDict.get(round)
        roundScore = moveValues.get(yourMove)

        result = round[1]

        if result == "Y":
            roundScore += 3
        elif result == "Z":
            roundScore += 6

        finalScore += roundScore

inputFile.close()

print(finalScore)