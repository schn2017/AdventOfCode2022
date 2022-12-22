import sys

class Node:
    def __init__(self, row, col, heightChar):
        self.row = row
        self.col = col
        self.height = self.convertHeightCharToInt(heightChar)
        self.isEnd = True if heightChar == "E" else False
        self.neighbors = []
        self.path = ''

    def convertHeightCharToInt(self, char):
        if char == "S":
            char = 'a'
        if char == "E":
            char = 'z'
        
        return ord(char) - 97

class HillClimbingAlgorithm:
    def __init__(self):
        self.startingPositions = []
        self.nodes = []
        self.directionRules = {
            "N": [-1, 0],
            "S": [1, 0],
            "E": [0, 1],
            "W": [0, -1]
        }

    def parseInputFile(self):
        inputFile = open(sys.argv[1], "r")
        currentRowIdx = 0

        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            self.nodes.append([])

            for index, char in enumerate(sanitizedLine):
                if char == "S" or char == "a":
                    self.startingPositions.append(Node(currentRowIdx, index, char))

                self.nodes[currentRowIdx].append(Node(currentRowIdx, index, char))

            currentRowIdx += 1
        inputFile.close()

    def setupNodes(self):
        for row in self.nodes:
            for node in row:
                self.addNeighbors(node)

    def addNeighbors(self, currentNode):
        if self.isDirectionValid(currentNode, "N"):
            currentNode.neighbors.append([currentNode.row - 1, currentNode.col])
        if self.isDirectionValid(currentNode, "S"):
            currentNode.neighbors.append([currentNode.row + 1, currentNode.col])
        if self.isDirectionValid(currentNode, "E"):
            currentNode.neighbors.append([currentNode.row, currentNode.col + 1])
        if self.isDirectionValid(currentNode, "W"):
            currentNode.neighbors.append([currentNode.row, currentNode.col - 1])

    def isDirectionValid(self, currentNode, direction):
        rowPos = currentNode.row + int(self.directionRules.get(direction)[0])
        colPos = currentNode.col + int(self.directionRules.get(direction)[1])

        # Check if row coordinate in bounds
        if rowPos < 0 or rowPos >= len(self.nodes):
            return False

        # Check if col coordinate in bounds
        if colPos < 0 or colPos >= len(self.nodes[0]):
            return False

        targetNode = self.nodes[rowPos][colPos]
        # Check if target height is greater than one elevation higher than current one
        if targetNode.height > currentNode.height + 1:
            return False

        return True

    def searchAllStartingPaths(self):
        pathLengths = []
        for startingPosition in self.startingPositions:
            pathLengths.append(self.search(startingPosition))
            self.clearPaths()
        shortestPath = min(pathLengths)
        print("The shortest path is " + str(shortestPath))

    def search(self, startingNode):
        search = [startingNode]
        visited = []
        while len(search) > 0:
            currentNode = search.pop(0)
            actualNode = self.nodes[currentNode.row][currentNode.col]
            positionString = str(currentNode.row) + "," + str(currentNode.col)

            if (positionString in visited) == False:
                if actualNode.isEnd:
                    actualNode.path += positionString
                    pathParts = actualNode.path.split("-->")

                    # Subtract starting spot since you aren't walking to it
                    return len(pathParts) - 1
                else:
                    visited.append(positionString)

                    for neighbor in actualNode.neighbors:
                        self.nodes[neighbor[0]][neighbor[1]].path = actualNode.path + " " + positionString + "-->"
                        search.append(self.nodes[neighbor[0]][neighbor[1]])

        return 999999

    def clearPaths(self):
        for row in self.nodes:
            for node in row:
                node.path = ''

def main():
    algo = HillClimbingAlgorithm()
    algo.parseInputFile()
    algo.setupNodes()
    algo.searchAllStartingPaths()

if __name__ == "__main__":
    main()