import sys
def main():
    device = Device()
    device.readInInstructions()
    device.process()

class Instruction:
    def __init__(self, value, operation,  startCycle):
        self.value = value
        self.operation = operation
        self.completionCycle = startCycle + 1 if operation == "addx" else startCycle
        pass

class Device:
    def __init__(self):
        self.registerValue = 1
        self.cycle = 1
        self.instructions = []
        self.signalStrengthChecks = [20, 60, 100, 140, 180, 220]
        self.signalStrengthSum = 0
        self.crt = [[],[],[],[],[],[]]
        self.currentRow = 0
        pass

    def readInInstructions(self):
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            instruction = sanitizedLine.split(" ")
            startingCycle = self.instructions[len(self.instructions) - 1].completionCycle + 1 if len(self.instructions) > 0 else self.cycle

            if instruction[0] == "addx":
                newInstruction = Instruction(int(instruction[1]), instruction[0], startingCycle)
                self.instructions.append(newInstruction)
            elif instruction[0] == "noop":
                newInstruction = Instruction(0, instruction[0], startingCycle)
                self.instructions.append(newInstruction)


    def process(self):
        print("Sprite position: " + self.spritePositionString())

        while len(self.instructions) > 0:
            self.processCycle()
            print("")
        
        self.printCRTDisplay()

    def processCycle(self):

        # Update CRT
        self.setCRT()

        # Handle any instructions that just completed
        if len(self.instructions) > 0 and self.instructions[0].completionCycle == self.cycle:
            self.registerValue += self.instructions[0].value
            print("End of cycle " + str(self.cycle) + ": finish executing " 
                + self.instructions[0].operation + " " + str(self.instructions[0].value) 
                + " (Register X is now " + str(self.registerValue) + ")")

            print("Sprite position: " + self.spritePositionString())
            self.instructions.pop(0)

        self.cycle += 1

    def setCRT(self):
        if len(self.crt[self.currentRow]) == 40:
            self.currentRow += 1

        rowOffset = 40 * self.currentRow
        start = self.registerValue - 1 + rowOffset
        middle = self.registerValue + rowOffset
        end = self.registerValue + 1 + rowOffset


        print("At cycle " + str(self.cycle) + " start: " +str(start) +", middle: "+ str(middle) + ". end:" + str(end))

        # Need to subtract 1 from cycle in order to sync with pixl position for exmaple cycle 10 corresponds with position 9
        if self.cycle - 1 == start or self.cycle - 1 == middle or self.cycle  -1 == end:
            self.crt[self.currentRow].append("#")
        else:
            self.crt[self.currentRow].append(".")

        self.printCRTRow()
            

    def printCRTRow(self):
        print("During cycle " + str(self.cycle) + ": CRT draws pixel in position " + str(self.cycle - 1))
        print("Current CRT Row: " + ''.join(self.crt[self.currentRow]))

    def spritePositionString(self):
        start = self.registerValue - 1
        middle = self.registerValue
        end = self.registerValue + 1
        spriteStr = ""
        for x in range(0, 40):
            if x == start or x == middle or x == end:
                spriteStr += "#"
            else:
                spriteStr += "."
        return spriteStr

    def printCRTDisplay(self):
        for row in self.crt:
            print(''.join(row))


if __name__ == "__main__":
    main()