import sys
def main():
    cpu = CPU()
    cpu.readInInstructions()
    cpu.process()

class Instruction:
    def __init__(self, value, operation,  startCycle):
        self.value = value
        self.operation = operation
        self.completionCycle = startCycle + 1 if operation == "addx" else startCycle

class CPU:
    def __init__(self):
        self.registerValue = 1
        self.cycle = 1
        self.instructions = []
        self.signalStrengthChecks = [20, 60, 100, 140, 180, 220]
        self.signalStrengthSum = 0

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
        while len(self.instructions) > 0:
            self.processCycle()
        print("The total signal strength is " + str(self.signalStrengthSum))

    def processCycle(self):
        # Add signal strength if at pre determined cycle
        if self.cycle in self.signalStrengthChecks:
            self.signalStrengthSum += self.cycle * self.registerValue
            print("During the " + str(self.cycle) + "th cycle, register X has the value " 
                + str(self.registerValue) + ", so the signal strength is " + str(self.cycle)  
                + " * " + str(self.registerValue) + " = " + str(self.cycle * self.registerValue))
        
        # Handle instruction
        if len(self.instructions) > 0 and self.instructions[0].completionCycle == self.cycle:
            self.registerValue += self.instructions[0].value
            self.instructions.pop(0)

        self.cycle += 1
if __name__ == "__main__":
    main()
