import sys

class Packet:
    def __init__(self, parent = None):
        self.parent = parent
        self.data = []

class PacketComparer:
    def __init__(self):
        self.pairs = []

    def compare(self, data, otherData, level):
        print('\t' * (level) + "Comparing " + str(data) + " vs " + str(otherData))
        for index in range(0, len(data)):
            # Index not available in other pair
            if index >= len(otherData):
                # If the right list runs out of items first, the inputs are not in the right order
                if len(data) > len(otherData) and type(data) == list and type(otherData) == list:
                    print('\t' * (level) + "-Right side ran out of items, so inputs are not in the right order")
                    return 0

            if type(data[index]) == int and type(otherData[index]) == int:
                print('\t' * (level) + " -Compare " + str(data[index]) + " vs " + str(otherData[index]))
                if (data[index] > otherData[index]):
                    print('\t' * (level + 1 ) + "-Right side is smaller, so inputs are not in the right order")
                    return 0
                elif data[index] < otherData[index]:
                    print('\t' * (level + 1) + "-Left side is smaller, so inputs are in the right order")
                    return 1
                else:
                    continue
            elif type(data[index]) == list and type(otherData[index]) == list:
                result = self.compare(data[index], otherData[index], level + 1)
                if result != -1:
                    return result
            elif (type(data[index]) == int and type(otherData[index]) == list):
                print('\t' * (level + 1)  + "Mixed types: convert left to [" + str(data[index]) + "] and retry comparison")
                result = self.compare([data[index]], otherData[index], level + 1)
                if result != -1:
                    return result
            elif (type(data[index]) == list and type(otherData[index]) == int):
                print('\t' * (level + 1) + "Mixed types: convert right to [" + str(otherData[index]) + "] and retry comparison")
                result = self.compare(data[index], [otherData[index]], level + 1)
                if result != -1:
                    return result
        
        #If the left list runs out of items first, the inputs are in the right order
        if len(data) < len(otherData) and type(data) == list and type(otherData) == list:
            print('\t' * (level) + "-Left side ran out of items, so inputs are in the right order")
            return 1
        return -1

    def compareAllPairs(self):
        sum = 0
        for index, pair in enumerate(self.pairs):
            print("Pairs "  +str(index + 1))
            result = self.compare(pair[0].data, pair[1].data, 0)
            if result == 1:
                print("Pair " + str(index + 1) + " is in order")
                sum += index + 1
            elif result == -1:
                print("Pair " + str(index + 1) + "returned -1")
                sum += index + 1

            elif result == 0:
                print("Pair " + str(index + 1) + " is not in order")

        print("The sum is " + str(sum))

    def parseInputFile(self):
        inputFile = open(sys.argv[1], "r")
        packet1 = Packet()
        packet2 = Packet()
        currentPacket = Packet()
        readingFirstPacket = True
        for line in inputFile:
            if len(line.strip()) == 0:
                continue
            charStr = ""
            for index, char in enumerate(line):
                if char == "[":
                    if index == 0:
                        if readingFirstPacket:
                            currentPacket = packet1
                        else:
                            currentPacket = packet2
                    else:
                        currentPacket = Packet(currentPacket)
                elif char == "]":
                    if len(charStr) > 0:
                        currentPacket.data.append(int(charStr))
                    charStr = ""

                    if readingFirstPacket:
                        if packet1 == currentPacket:
                            packet1.data = currentPacket.data
                        else:
                            currentPacket.parent.data.append(currentPacket.data)
                            currentPacket = currentPacket.parent
                    else:
                        if packet2 == currentPacket:
                            packet2.data = currentPacket.data
                        else:
                            currentPacket.parent.data.append(currentPacket.data)
                            currentPacket = currentPacket.parent
                elif char == ",":
                    if len(charStr) > 0:
                        currentPacket.data.append(int(charStr))
                    charStr = ""
                elif char.isdigit():
                    charStr += char

                if char == '\n':
                    # Switch over to reading second Packet in pair
                    if readingFirstPacket:
                        readingFirstPacket = False
                    else:
                        #reset everything for next pair parsing
                        readingFirstPacket = True
                        self.pairs.append([packet1, packet2])

                        packet1 = Packet()
                        packet2 = Packet()
        #Append last pair found
        self.pairs.append([packet1, packet2])

def main():
 solver = PacketComparer()
 solver.parseInputFile()
 solver.compareAllPairs()

if __name__ == "__main__":
    main()