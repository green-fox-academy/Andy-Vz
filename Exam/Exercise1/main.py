from collections import Counter # Import used for counting letters

input = "application"

def getUniqueLetters(input):
    # Split the input string into individual letters
    splitInput = list(input)
    # Extract the count of each letter in the splitInput list
    inputCount = Counter(splitInput).most_common()

    uniqueLetters = [] # List that holds the final output
    #Remove all the leters from the list with more than 1 occurance
    for letter in inputCount:
        if letter[1] < 2:
            uniqueLetters.append(letter[0])
    return uniqueLetters

# Trying a random
print("Geting unique letters from \"", input, "\"")
print(getUniqueLetters(input),"\n")


# Unit Test 1
unitTests = [
    {
        "input":"anagram",
        "output":["n", "g", "r", "m"]
     },{
        "input": "awareness",
        "output": ['w', 'r', 'n']
    }
]


# Run the unit tests
for unitTest in unitTests:
    if getUniqueLetters(unitTest["input"]) == unitTest["output"]:
        print("Unit test number", unitTests.index(unitTest) + 1 , " passed")
    else:
        print("Unit test number", unitTests.index(unitTest) + 1, " failed")
