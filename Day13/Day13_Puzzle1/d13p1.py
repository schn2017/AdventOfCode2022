import sys

class Packet:
    def __init__(self, parent = None):
        self.parent = parent
        self.contents = []

    def printContents(self):
        for content in self.contents:
            if isinstance(content, Packet):
                print("child packet found")
                content.printContents()
            else:
                print(content)

def main():
    inputFile = open(sys.argv[1], "r")
    pairs = []
    packet1 = Packet()
    packet2 = Packet()
    currentPacket = Packet()
    readingFirstPair = True
    nesting = 0
    for line in inputFile:
        if len(line.strip()) == 0:
            readingFirstPair = True
            nesting = 0
            pairs.append([packet1, packet2])

            packet1 = Packet()
            packet2 = Packet()
            continue

        for index, char in enumerate(line):
            if char == "[":
                if index == 0:
                    if readingFirstPair:
                        currentPacket = packet1
                    else:
                        currentPacket = packet2
                else:
                    nesting += 1
                    currentPacket = Packet(currentPacket)
            elif char == "]":
                if readingFirstPair:
                    if nesting == 0:
                        packet1.contents = currentPacket.contents
                    else:
                        currentPacket.parent.contents.append(currentPacket.contents)
                        currentPacket = currentPacket.parent
                        nesting -=1

                else:
                    if nesting == 0:
                        packet2.contents = currentPacket.contents
                    else:
                        currentPacket.parent.contents.append(currentPacket.contents)
                        currentPacket = currentPacket.parent
                        nesting -=1
            elif char == ",":
                pass
            elif char.isdigit():
                currentPacket.contents.append(int(char))

            if char == '\n':
                readingFirstPair = False
                nesting = 0

    for pair in pairs:
        print("part 1")
        print(pair[0].contents)
        print('Length is ' + str(len(pair[0].contents)))
        print("part 2")
        print(pair[1].contents)
        print('Length is ' + str(len(pair[1].contents)))
        print("")


    inputFile.close()

if __name__ == "__main__":
    main()