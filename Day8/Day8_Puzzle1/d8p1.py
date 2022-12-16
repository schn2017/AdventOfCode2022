import sys

class Tree:
    def __init__(self, height, rowPos, colPos):
        self.height = height
        self.rowPos = rowPos
        self.colPos = colPos
        self.isEdge = False

    def checkIfEdge(self, row, column, width, height):
        return row == 0 or row == width - 1 or column == 0 or column == height - 1
        
def solve():
    inputFile = open(sys.argv[1], "r")
    
    trees = []
    rowCount = 0
    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
        row = []
        colCount = 0
        for char in sanitizedLine:
            newTree = True(int(char), rowCount, colCount)
            row.append(newTree)
            colCount += 1
        trees.append(row)
        rowCount += 1

    visibleTreeCount(trees)

    inputFile.close() 

def main():
    inputFile = open(sys.argv[1], "r")
    
    trees = []
    rowCount = 0
    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
        row = []
        for char in sanitizedLine:
            row.append(int(char))
        trees.append(row)
        rowCount += 1

    visibleTreeCount(trees)

    inputFile.close()

def visibleTreeCount(trees):
    width = len(trees[0])
    height = len(trees)

    # Subtract two from height multiplication to take into account first and last rows
    perimeterTreesCnt = 2 * width + 2 * (height - 2)

    print("There are " + str(perimeterTreesCnt) + " visible trees around the perimeter")
    totalVisibleTrees = perimeterTreesCnt
    for row in range(1, len(trees) - 1):
        rowStr = ""
        for column in range(1, width - 1):
            rowStr += str(trees[row][column])
            #print('Checking ' + str(trees[row][column]) + " at position " + str(row) + "," + str(column))

            if checkDirections(trees, row, column, 0):
                totalVisibleTrees += 1
    
    print("Height is " + str(height))
    print("Width is " + str(width))
    print("The area is " + str(height * width))
    print("There are " + str(perimeterTreesCnt) + " visible trees around the perimeter")
    print("There are " + str(totalVisibleTrees) + " trees visible")

def checkDirections(trees, row, column, level):
    print("Level "  + str (level))

     #North
    if trees[row][column] > trees[row - 1][column]:
        if isTreeVisible(trees, row, column, row - 1, column, level + 1):
            return True
        else:
            if checkDirections(trees, row - 1, column, level + 1):
                return True
    # South
    if trees[row][column] > trees[row + 1][column]:
        if isTreeVisible(trees, row, column, row + 1, column, level + 1):
            return True
        else:
            if checkDirections(trees, row + 1, column, level + 1):
                return True
    # East
    if trees[row][column] > trees[row][column + 1]:
        if isTreeVisible(trees, row, column, row, column + 1, level + 1):
            return True
        else:
            if checkDirections(trees, row, column + 1, level + 1):
                return True
    # West
    if trees[row][column] > trees[row][column - 1]:
        if isTreeVisible(trees, row, column, row, column - 1, level + 1):
            return True
        else:
            if checkDirections(trees, row, column - 1, level + 1):
                return True
    return False


def isTreeVisible(trees, row, column, dirRow, dirCol, level):
    #print("Level "  + str (level))

    if trees[row][column] > trees[dirRow][dirCol]:
        if isEdge(len(trees[0]), len(trees), dirRow, dirCol):
            return True
    return False

def isEdge(width, height, row, column):
    return row == 0 or row == width - 1 or column == 0 or column == height - 1

if __name__ == "__main__":
    main()