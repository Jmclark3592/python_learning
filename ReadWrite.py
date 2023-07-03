def writeToFile(filename, text):
    with open(filename, "w") as fileObj:
        fileObj.write(text)


def appendToFile(filename, text):
    with open(filename, "a") as fileObj:
        fileObj.write(text)


def readFromFile(filename):
    with open(filename) as fileObj:
        return fileObj.read()


writeToFile("greet.md", "Hello!\n")
appendToFile("greet.md", "Goodbye!\n")
assert readFromFile("greet.md") == "Hello!\nGoodbye!\n"
