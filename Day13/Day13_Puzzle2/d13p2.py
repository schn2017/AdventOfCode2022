import sys

class Packet:
    def __init__(self, parent = None):
        self.parent = parent
        self.data = []

class PacketComparer:
    def __init__(self):
        self.packets = []

    def compare(self, data, otherData):
        for index in range(0, len(data)):
            # Index not available in other pair
            if index >= len(otherData):
                # If the right list runs out of items first, the inputs are not in the right order
                if len(data) > len(otherData) and type(data) == list and type(otherData) == list:
                    return 0

            if type(data[index]) == int and type(otherData[index]) == int:
                if (data[index] > otherData[index]):
                    return 0
                elif data[index] < otherData[index]:
                    return 1
                else:
                    continue
            elif type(data[index]) == list and type(otherData[index]) == list:
                result = self.compare(data[index], otherData[index])
                if result != -1:
                    return result
            elif (type(data[index]) == int and type(otherData[index]) == list):
                result = self.compare([data[index]], otherData[index])
                if result != -1:
                    return result
            elif (type(data[index]) == list and type(otherData[index]) == int):
                result = self.compare(data[index], [otherData[index]])
                if result != -1:
                    return result
        
        #If the left list runs out of items first, the inputs are in the right order
        if len(data) < len(otherData) and type(data) == list and type(otherData) == list:
            return 1
        return -1

    def setup(self):
        self.parseInputFile()

        # Add Divider Packet with data [[2]]
        packet2 = Packet()
        packet2.data.append([2])
        self.packets.append(packet2)

        # Add Divider Packet with data [[6]]
        packet6 = Packet()
        packet6.data.append([6])
        self.packets.append(packet6)

    def bubbleSort(self):
        isSorted = False
        while isSorted == False:
            sortCount = 0
            for index in range(0, len(self.packets)):
                if index >= len(self.packets) or index + 1 >= len(self.packets):
                    break
                
                left = self.packets[index].data
                right = self.packets[index + 1].data

                if self.compare(left, right) == False:
                    tmp = left
                    self.packets[index].data = right
                    self.packets[index + 1].data = tmp
                else:
                    sortCount += 1
                
                if sortCount == len(self.packets) - 1:
                    isSorted = True

    def parseInputFile(self):
        inputFile = open(sys.argv[1], "r")
        packet1 = Packet()
        currentPacket = Packet()
        for line in inputFile:
            if len(line.strip()) == 0:
                continue
            charStr = ""
            for index, char in enumerate(line):
                if char == "[":
                    if index == 0:
                        currentPacket = packet1
                    else:
                        currentPacket = Packet(currentPacket)
                elif char == "]":
                    if len(charStr) > 0:
                        currentPacket.data.append(int(charStr))
                    charStr = ""
                    if packet1 == currentPacket:
                        packet1.data = currentPacket.data
                    else:
                        currentPacket.parent.data.append(currentPacket.data)
                        currentPacket = currentPacket.parent
                elif char == ",":
                    if len(charStr) > 0:
                        currentPacket.data.append(int(charStr))
                    charStr = ""
                elif char.isdigit():
                    charStr += char

            self.packets.append(packet1)
            packet1 = Packet()

    def solve(self):
        self.setup()
        self.bubbleSort()
        product = 1
        for index, packet in enumerate(self.packets):
           if packet.data == [[2]] or packet.data == [[6]]:
               product *= (index + 1)

        print("The decoder key is " + str(product))
def main():
 solver = PacketComparer()
 solver.solve()


if __name__ == "__main__":
    main()