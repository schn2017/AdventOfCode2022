import re

moveValues = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

rulesDict = {
    "AX": "D",
    "AY": "W",
    "AZ": "L",
    "BX": "L",
    "BY": "D",
    "BZ": "W",
    "CX": "W",
    "CY": "L",
    "CZ": "D"
}

inputFile = open("input.txt", "r")
finalScore = 0 


for line in inputFile:
    if (len(line.strip()) > 0):
        round = re.sub(r'\W+', '', line)

        yourMove = round[1] 
        roundScore =  moveValues.get(yourMove)

        result = rulesDict.get(round)

        if result == "W":
            roundScore += 6
        elif result == "D":
            roundScore += 3
        
        finalScore += roundScore

inputFile.close()

print(finalScore)
