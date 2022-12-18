import sys
import math

class Node:
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
    head = Node(0,0)
    tail = Node(0,0)
    tailVisited.append(str(tail.x) + "," + str(tail.y))

    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
        direction = sanitizedLine.split(" ")[0]
        magnitude = int(sanitizedLine.split(" ")[1])

        for x in range(0, magnitude):
            xIncrease = directionRules.get(direction)[0]
            yIncrease = directionRules.get(direction)[1]

            # original head position
            originalX = tail.x
            originalY = tail.y

            # Move head
            head.x += xIncrease
            head.y += yIncrease

            # Figure out distance
            yDistance = abs(head.y - tail.y)
            xDistance = abs(head.x - tail.x)
            sum = (yDistance * yDistance)+ (xDistance * xDistance)
            distanceFrom = math.sqrt(sum)
            # diagonally adjacent, no movement needed
            if distanceFrom == math.sqrt(2):
                continue

            # Vertical movement
            if yDistance == 2 and xDistance == 0:
                tail.y = tail.y + yIncrease
            # Horizontal movement
            elif xDistance == 2 and yDistance == 0:
                tail.x = tail.x + xIncrease
            # Diagonal movement
            elif distanceFrom > math.sqrt(2):
                tail.x += 1 if head.x - tail.x > 0 else -1
                tail.y += 1 if head.y - tail.y > 0 else -1

            # Add to list of movenents if either position coordinate changed
            if originalX != tail.x or originalY != tail.y:
                tailVisited.append(str(tail.x) + "," + str(tail.y))


    uniqueVisits = set(tailVisited)

    #print(uniqueVisits)

    print("The tail visited " + str(len(uniqueVisits)) + " unique spots")
    
    inputFile.close()

if __name__ == "__main__":
    main()