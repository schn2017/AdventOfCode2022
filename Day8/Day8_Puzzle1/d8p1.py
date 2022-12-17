import sys

class Tree:
    def __init__(self, height, rowPos, colPos):
        self.height = height
        self.rowPos = rowPos
        self.colPos = colPos
        self.isEdge = False
        self.isVisible = False

    def checkIfEdge(self, width, height):
        self.isEdge = self.rowPos == 0 or self.rowPos == width - 1 or self.colPos == 0 or self.colPos == height - 1
        self.isVisible = self.isEdge

class Solution:
    def __init__(self):
        self.visibleTrees = 0
        self.width = 0
        self.height = 0
        self.trees = []
        self.path = []

    def printPath(self):
        path = ""
        read = []

        for tree in self.path:
            path += str(tree.rowPos) + "," +str(tree.colPos) + " height " + str(tree.height) + " "

            if tree.isEdge:
                path+= "EDGE "
                break

            if tree != self.path[len(self.path) - 1]:
                path += "--> "
            else:
                path += " DONE"
            read.append(tree)
        print(path)


    def solve(self):
        self.parseInputFile()
        
        # find edges
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                tree.checkIfEdge(self.width, self.height)
                if tree.isEdge:
                   self.visibleTrees += 1

        # Find visible non edge trees
        for rowOfTrees in self.trees:
            for tree in rowOfTrees:
                if tree.isEdge == True:
                    continue

                if self.isTreeVisible(tree):
                    self.visibleTrees += 1
                    self.printPath()
                self.path = []

        # Print visible edge rocks count
        print(str(self.visibleTrees) + " visible edge trees")

    def isTreeVisible(self, tree):
        self.path.append(tree)

        if tree.isEdge:
            return True

        #check if tree is visible
        #print("Checking non edge tree of height " + str(tree.height) + " at " + str(tree.rowPos) + "," +str(tree.colPos))
        row = tree.rowPos
        col = tree.colPos

        if tree.height > self.trees[row][col - 1].height:
            # check if other tree is visible
            tree.isVisible = self.isTreeVisible(self.trees[row][col - 1])
            
            if tree.isVisible:
                return True

        if tree.height > self.trees[row][col + 1].height:
            tree.isVisible = self.isTreeVisible(self.trees[row][col + 1])
            if tree.isVisible:
                return True

        if tree.height > self.trees[row + 1][col].height:
            tree.isVisible = self.isTreeVisible(self.trees[row + 1][col])
            if tree.isVisible:
                return True

        if tree.height > self.trees[row - 1][col].height:
            tree.isVisible = self.isTreeVisible(self.trees[row - 1][col])
            if tree.isVisible:
                return True

        if len(self.path) > 0:        
            self.path.pop()
        return False

    def parseInputFile(self):    
        inputFile = open(sys.argv[1], "r")

        rowCount = 0

        for line in inputFile:
            row = []
            colCount = 0
            sanitizedLine = line.replace("\n", "")
            for char in sanitizedLine:
                newTree = Tree(int(char), rowCount, colCount)
                row.append(newTree)
                colCount += 1
            self.trees.append(row)
            rowCount += 1

        inputFile.close()

        self.width = len(self.trees[0])
        self.height = len(self.trees)

    def printInfo(self):
        width = len(self.trees[0])
        height = len(self.trees)

        # Subtract two from height multiplication to take into account first and last rows
        perimeterTreesCnt = 2 * width + 2 * (height - 2)
        print("Height is " + str(height))
        print("Width is " + str(width))
        print("The area is " + str(height * width))
        print("There are " + str(perimeterTreesCnt) + " visible trees around the perimeter")

def main():
    solution = Solution()
    solution.solve()

if __name__ == "__main__":
    main()