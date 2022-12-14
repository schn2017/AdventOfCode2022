import sys
def main():
    inputFile = open(sys.argv[1], "r")
    for line in inputFile:
        sanitizedLine = line.replace("\n", "")
        chars = []
        processed = 0
        for char in sanitizedLine:
            uniqueChars = set(chars)
            if len(uniqueChars) == 14 and chars.count(char) == 0:
                print("Marker found " + char)
                print(str(processed) + " chars")
                chars = []
                break

            if len(chars) == 14:
                chars.pop(0)
            chars.append(char)   
            processed += 1
    
            
    inputFile.close()

if __name__ == "__main__":
    main()