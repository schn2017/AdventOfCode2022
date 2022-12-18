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
        # Establish edges
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                tree.checkIfEdge(width, height)


        # Find visible non edge trees
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                self.currentTreeHeight = tree.height
                if tree.isEdge == True:
                    self.visibleTrees += 1
                    continue

                if self.checkDirections(tree):
                    self.visibleTrees += 1
                self.path = []

        print(str(self.visibleTrees) + " visible trees")

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

    def checkDirections(self, tree):
        return self.isVisible(tree, "N", True) or self.isVisible(tree, "S", True) or self.isVisible(tree, "E", True) or self.isVisible(tree, "W", True)

    def isVisible(self, tree, direction, isFirstTree):
        if isFirstTree:
            self.path = []

        self.path.append(tree)
        otherTree = self.trees[tree.rowPos + self.directionRules.get(direction)[0]][tree.colPos + self.directionRules.get(direction)[1]]

        if self.currentTreeHeight > otherTree.height:
            if otherTree.isEdge:
                self.path.append(otherTree)
                return True
            else:
                return self.isVisible(otherTree, direction, False)
        return False

def main():
    solution = Solution()
    solution.solve()

if __name__ == "__main__":
    main()