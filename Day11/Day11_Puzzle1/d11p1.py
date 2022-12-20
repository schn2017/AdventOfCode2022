import sys
from datetime import datetime

class TossedItem:
    def __init__(self, worryLevel, target):
        self.worryLevel = worryLevel
        self.target = target

class Monkey:
    def __init__(self):
        self.items = []
        self.itemsInspected = 0
        self.itemsToToss = []

        # Operation members
        self.operator = ''
        self.operationAmount = ''

        # Info used when throwing item to other monkeys
        self.divideBy = 1
        self.otherMonkeyIfTrue = 0
        self.otherMonkeyIfFalse = 0

    def inspectItems(self):
        for index in range(0, len(self.items)):
            self.items[index] = self.performOperation(self.items[index]) // 3
            self.itemsInspected += 1
            self.tossItem(self.items[index])

    def tossItem(self, item):
        if item % self.divideBy == 0:
            self.itemsToToss.append(TossedItem(item, self.otherMonkeyIfTrue)) 
        else:
            self.itemsToToss.append(TossedItem(item, self.otherMonkeyIfFalse)) 


    def performOperation(self, item):
        newValue = 0
        amountValue = item if self.operationAmount == "old" else int(self.operationAmount)

        if self.operator == "+":
            newValue = item + amountValue
        elif self.operator == "*":
            newValue = item * amountValue
        return newValue

    def printMonkey(self):
        print("  Starting Items: " + ', '.join(map(str, self.items)))
        print("  Operation: new = old " + self.operator + " " + self.operationAmount)
        print("  Test: divisible by " + str(self.divideBy))
        print("    If true: throw to monkey " + str(self.otherMonkeyIfTrue))
        print("    If false: throw to monkey " + str(self.otherMonkeyIfFalse))

class MonkeyBusiness:
    def __init__(self, rounds):
        self.monkeys = []
        self.rounds = rounds

    def parseInputFile(self):
        currentMonkeyIdx = 0
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            sanitizedLine = sanitizedLine.strip()
            parts = sanitizedLine.split(" ")
            if parts[0] == "Monkey":
                currentMonkeyIdx = len(self.monkeys)
                self.monkeys.append(Monkey())
            elif parts[0] == "Starting":
                items = sanitizedLine.split(":")[1].split(",")
                for item in items:
                    self.monkeys[currentMonkeyIdx].items.append(int(item))
            elif parts[0] == "Operation:":
                self.monkeys[currentMonkeyIdx].operator = parts[4]
                self.monkeys[currentMonkeyIdx].operationAmount = parts[5]
            elif parts[0] == "Test:":
                self.monkeys[currentMonkeyIdx].divideBy = int(parts[3])
            elif parts[0] == "If" and parts[1] == "true:":
                self.monkeys[currentMonkeyIdx].otherMonkeyIfTrue = int(parts[5])
            elif parts[0] == "If" and parts[1] == "false:":
                self.monkeys[currentMonkeyIdx].otherMonkeyIfFalse = int(parts[5])
        inputFile.close()

    def performRounds(self):
        totalTimeTaken: deltaTime = datetime.now() - datetime.now()
        for round in range(0, self.rounds):
            rountStartTime = datetime.now()
            print("Performing round " + str(round))
            self.performRound()
            roundEndTime = datetime.now()

            deltaTime = roundEndTime - rountStartTime
            totalTimeTaken += deltaTime
            print("Round took " + str(deltaTime.total_seconds() * 1000) + " microseconds")
        print("Total Time Taken " + str(totalTimeTaken.total_seconds()) + " seconds\n")
        self.getTopTwoMonkeyBusiness()

    def performRound(self):
        for index, monkey in enumerate(self.monkeys):
            print("Monkey " + str(index))
            monkey.inspectItems()

            for tossedItem in monkey.itemsToToss:
                self.monkeys[tossedItem.target].items.append(tossedItem.worryLevel)

            self.monkeys[index].itemsToToss = []
            self.monkeys[index].items = []
        print("\n")
        print("End of round results")
        for index, monkey in enumerate(self.monkeys):
            print("Monkey " + str(index) + ": " + ', '.join(map(str, monkey.items)))

    def getTopTwoMonkeyBusiness(self):
        mostItemsInspected =  0
        secondMostItemscounted = 0
        print("End of rounds results")
        for index, monkey in enumerate(self.monkeys):
            print("Monkey " + str(index) + ": inspected " + str(monkey.itemsInspected) + " items")
            if monkey.itemsInspected > mostItemsInspected:
                secondMostItemscounted = mostItemsInspected
                mostItemsInspected = monkey.itemsInspected
            elif monkey.itemsInspected > secondMostItemscounted:
                secondMostItemscounted = monkey.itemsInspected
        print("")
        print("Top two monkey business is " + str(mostItemsInspected ) + " * " + str(secondMostItemscounted) +  " = " + str(mostItemsInspected * secondMostItemscounted))

    def displayMonkeys(self):
        for index, monkey in enumerate(self.monkeys):
            print("Monkey " + str(index))
            monkey.printMonkey()
    

def main():
    monkeyBusiness = MonkeyBusiness(20)
    monkeyBusiness.parseInputFile()
    monkeyBusiness.displayMonkeys()
    monkeyBusiness.performRounds()

if __name__ == "__main__":
    main()