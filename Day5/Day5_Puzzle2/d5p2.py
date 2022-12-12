import sys
from enum import Enum

class Instruction:
    def __init__(self, moves, source, destination):
        self.moves = moves
        self.source = source
        self.destination = destination

class Solution:
    def __init__(self):
        self.stacks = []
        self.instructions = []
        self.parserState = "PICTURE"

    def parseInput(self):
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            sanitizedLine = line.replace("\n", "")

            # Skip crate numbering line and move to instruction parsing
            if line[0] == " " and line[1] == "1" and line[2] == " ":
                self.parserState = "INSTRUCTIONS"
                continue

            if self.parserState == "PICTURE":
                self.parsePicture(sanitizedLine)
            else:
                self.parseInstructions(sanitizedLine)

        inputFile.close()

    def parsePicture(self, line):
        readLine = line
        column = 0
        initialStackLength = len(self.stacks)
        while len(readLine) > 0:
            buffer = readLine[:3]

            # Intialize empty lists per stack
            if (initialStackLength == 0):
                self.stacks.append([])

            # Populate stack with crate
            if buffer[1].isalpha() == True:
                self.stacks[column].append(buffer[1])

            # Move to next 3 characters or 4 if there is a space
            if len(readLine) >= 4 and readLine[3] == " ":
                readLine = readLine[4:]
            else:
                readLine = readLine[3:]

            column += 1

    def parseInstructions(self, line):
        checkSpaces = line.replace(" ", "")

        if len(checkSpaces) >= 3:
            parts = line.split(" ")
            moves = int(parts[1])
            sourceCrate = int(parts[3])
            destinationCrate = int(parts[5])
            newInstruction = Instruction(moves, sourceCrate, destinationCrate)
            self.instructions.append(newInstruction)

    def executeInstructions(self):
        for instruction in self.instructions:
            destIndex = instruction.destination - 1
            sourceIndex = instruction.source - 1

            crateHolder = []

            for move in range(instruction.moves):
                # Get top crate from source and remove crate from source stack
                crate = self.stacks[sourceIndex].pop(0)
                crateHolder.append(crate)
            
            #Reverse crates to maintain order when placing in new stack
            crateHolder.reverse()

            # Add crates to top of destination stack
            for crate in crateHolder:
                self.stacks[destIndex].insert(0, crate)

    def topOfAllStacks(self):
        ret = ""

        for stack in self.stacks:
            ret += stack[0]

        return ret

    def solve(self): 
        self.parseInput()
        self.executeInstructions()
        print("Top of each stack is "  + self.topOfAllStacks())

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()