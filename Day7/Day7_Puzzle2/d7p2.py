import sys

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:    
    def __init__(self, name = "/", parentDirectory = None):
        self.name = name
        self.size = 0
        self.parentDirectory: Directory = parentDirectory
        self.childDirectories: list[Directory] = []
        self.files: list[File] = []

    def calculateFileSize(self):
        for file in self.files:
            self.size += file.size

        for directory in self.childDirectories:
            directory.calculateFileSize()
            self.size += directory.size

    def print(self, level = 0):
        print('\t' * (level) + "- " + self.name + " (dir, size=" + str(self.size)  + ")")
        for directory in self.childDirectories:
            directory.print(level + 1)
        for file in self.files:
            print('\t' * (level + 1) + "- " + file.name + " (file, size=" + str(file.size) + ")")
    
    def solvePuzzle1(self, cummulativeSum = 0):
        sum = 0

        if self.size <= 100000:
            sum = self.size
        
        for directory in self.childDirectories:
            childDirectorySize = directory.solvePuzzle1(cummulativeSum)
            sum += childDirectorySize

        return sum

    def solvePuzzle2(self, limit, directoryToBeDeletedSize):
        size = directoryToBeDeletedSize
        if self.size >= limit and self.size < directoryToBeDeletedSize:
            size = self.size

        for directory in self.childDirectories:
            newSize = directory.solvePuzzle2(limit, size)
            if newSize < size:
                size = newSize
        return size

class FileSystem: 
    def __init__(self):
        self.headDirectory: Directory = Directory()
        self.currentDirectory: Directory = self.headDirectory   

    def parseInputFile(self):
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            if sanitizedLine[0] == "$":
                self.handleChangeDirectoryCmd(sanitizedLine)
            elif sanitizedLine[0].isdigit():
                self.createFileAndAddToCurrentDirectory(sanitizedLine)
            elif sanitizedLine[:3] == "dir":
                self.createDirectoryAndAddToCurrentDirectory(sanitizedLine)

        inputFile.close()
    
    def handleChangeDirectoryCmd(self, line):
        cmdParts = line.split(" ")

        if cmdParts[1] == "cd":
            if cmdParts[2] == "/":
                self.currentDirectory = self.headDirectory
            elif cmdParts[2] == "..":
                self.currentDirectory = self.currentDirectory.parentDirectory
            else:
                self.goToChildDirectory(cmdParts[2])
        elif cmdParts[1] == "ls":
            self.printWorkingDirectory()

    def goToChildDirectory(self, childDirectoryName):
        for childDirectory in self.currentDirectory.childDirectories:
            if childDirectory.name == childDirectoryName:
                self.currentDirectory = childDirectory
                break
    
    def createFileAndAddToCurrentDirectory(self, line):
        cmdParts = line.split(" ")
        newFile = File(cmdParts[1], int(cmdParts[0]))
        self.currentDirectory.files.append(newFile)

    def createDirectoryAndAddToCurrentDirectory(self, line):
        cmdParts = line.split(" ")
        newDirectory = Directory(cmdParts[1], self.currentDirectory)
        self.currentDirectory.childDirectories.append(newDirectory)

    def printWorkingDirectory(self):
        print("--------------------------------------------------------------------------- ")
        self.currentDirectory.print()    

    def calculateFileSystemSize(self):
        self.headDirectory.calculateFileSize()

    def print(self):
        print("---------------------------------------------------------------------------- ")
        print("Full Directory Tree Below")
        self.headDirectory.print()

    def solvePuzzle2(self):
        currentFreeSpace = 70000000 - self.headDirectory.size
        print('The current free space is ' + str(currentFreeSpace))
        spaceNeededForUpdate = 30000000 - currentFreeSpace 
        print('The space needed to process the update is ' + str(spaceNeededForUpdate))
        print(self.headDirectory.solvePuzzle2(spaceNeededForUpdate, self.headDirectory.size))

def main():
    fileSystem = FileSystem()
    fileSystem.parseInputFile()
    fileSystem.calculateFileSystemSize()
    fileSystem.solvePuzzle2()


if __name__ == "__main__":
    main()