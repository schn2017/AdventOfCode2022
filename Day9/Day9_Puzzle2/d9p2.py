import sys
def main():
    inputFile = open(sys.argv[1], "r")
    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
    inputFile.close()

if __name__ == "__main__":
    main()