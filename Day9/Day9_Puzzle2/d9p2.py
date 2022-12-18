import sys
import math

class Knot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    inputFile = open(sys.argv[1], "r")
    directionRules = {
        "U": [0, 1],
        "D": [0, -1],
        "R": [1, 0],
        "L": [-1, 0]
    }
    tailVisited = []
    knots = []

    for x in range(0, 10):
        newKnot = Knot(0,0)
        knots.append(newKnot)

    tailVisited.append(str(knots[-1].x) + "," + str(knots[-1].y))

    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
        direction = sanitizedLine.split(" ")[0]
        magnitude = int(sanitizedLine.split(" ")[1])

        for x in range(0, magnitude):
            xIncrease = directionRules.get(direction)[0]
            yIncrease = directionRules.get(direction)[1]

            # original tail (last knot) position
            originalX = knots[-1].x
            originalY = knots[-1].y

            # Move head
            knots[0].x += xIncrease
            knots[0].y += yIncrease

            for knotIdx in range(1, len(knots)):
                moveKnot(knots[knotIdx - 1], knots[knotIdx])

            # Add to list of movenents if either position coordinate changed
            if originalX != knots[-1].x or originalY != knots[-1].y:
                tailVisited.append(str(knots[-1].x) + "," + str(knots[-1].y))

    uniqueVisits = set(tailVisited)
    print("The tail visited " + str(len(uniqueVisits)) + " unique spots")
    
    inputFile.close()

def moveKnot(previousKnot, currentKnot):
    # Figure out distance
    yDistance = abs(previousKnot.y - currentKnot.y)
    xDistance = abs(previousKnot.x - currentKnot.x)
    sum = (yDistance * yDistance)+ (xDistance * xDistance)
    distanceFrom = math.sqrt(sum)
    # diagonally adjacent, no movement needed
    if distanceFrom == math.sqrt(2):
        return
    # Vertical movement
    if yDistance == 2 and xDistance == 0:
        currentKnot.y += 1 if previousKnot.y - currentKnot.y > 0 else -1
    # Horizontal movement
    elif xDistance == 2 and yDistance == 0:
        currentKnot.x += 1 if previousKnot.x - currentKnot.x > 0 else -1
    # Diagonal movement
    elif distanceFrom > math.sqrt(2):
        currentKnot.x += 1 if previousKnot.x - currentKnot.x > 0 else -1
        currentKnot.y += 1 if previousKnot.y - currentKnot.y > 0 else -1

if __name__ == "__main__":
    main()