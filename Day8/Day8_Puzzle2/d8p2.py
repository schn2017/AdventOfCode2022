import sys

class Tree:
    def __init__(self, height, rowPos, colPos):
        self.height = height
        self.rowPos = rowPos
        self.colPos = colPos
        self.isEdge = False

    def checkIfEdge(self, width, height):
        self.isEdge = self.rowPos == 0 or self.rowPos == width - 1 or self.colPos == 0 or self.colPos == height - 1

class Solution:
    def __init__(self):
        self.visibleTrees = 0
        self.trees = []
        self.path = []
        self.currentTreeHeight = 0
        self.directionRules = {
            "N": [-1, 0],
            "S": [1, 0],
            "E": [0, 1],
            "W": [0, -1]
        }

    # Method used for debugging to visualize path being taken
    def printPath(self):
        path = ""
        read = []

        for tree in self.path:
            path += str(tree.rowPos) + "," +str(tree.colPos) + " height " + str(tree.height) + " "

            if tree.isEdge:
                path+= "EDGE "

            if tree != self.path[len(self.path) - 1]:
                path += "--> "
            read.append(tree)
        print(path)

    def solve(self):
        self.parseInputFile()
        width = len(self.trees[0])
        height = len(self.trees)
        bestScore = 0

        # Establish edges
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                tree.checkIfEdge(width, height)

        # get Scenic score of trees
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                self.currentTreeHeight = tree.height

                score = self.getScenicScore(tree)
                if score > bestScore:
                     bestScore = score

        print("The best score is " + str(bestScore))

    def parseInputFile(self):    
        inputFile = open(sys.argv[1], "r")

        rowCount = 0
        for line in inputFile:
            sanitizedLine = line.replace("\n", "")

            row = []
            colCount = 0
            for char in sanitizedLine:
                newTree = Tree(int(char), rowCount, colCount)
                row.append(newTree)
                colCount += 1

            self.trees.append(row)
            rowCount += 1

        inputFile.close()

    def getScenicScore(self, tree):
        return (
            self.getDirectionScenicScore(tree, "N") 
            * self.getDirectionScenicScore(tree, "S") 
            * self.getDirectionScenicScore(tree, "E") 
            * self.getDirectionScenicScore(tree, "W")
        )

    def getDirectionScenicScore(self, tree, direction):
        row = tree.rowPos + self.directionRules.get(direction)[0]
        col = tree.colPos + self.directionRules.get(direction)[1]

        # out of bounds
        if row < 0 or row >= len(self.trees) or col < 0 or col >= len(self.trees[0]):
            return 0

        otherTree = self.trees[row][col]

        if self.currentTreeHeight > otherTree.height:
            if otherTree.isEdge:
                return 1
            return 1 + self.getDirectionScenicScore(otherTree, direction)
        return 1

def main():
    solution = Solution()
    solution.solve()

if __name__ == "__main__":
    main()