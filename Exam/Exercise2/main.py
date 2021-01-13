# Write a method which can read and parse a file containing information about the average temperature of three European countries to raise awareness of climate change. Each line represents the average temperature of each country in the given year. The actual year can be found at the end of each line.
# The method should return the first coldest and hottest year in each country.
# The application should write the data to the console as key => value pairs.

resultsPath = 'C:\\Users\\carlo\\Desktop\\Andy-Vz\\Exam\\ibs-2020-10-coding-fundamentals-normal-exam\\results.txt'
allFrTemps = []
allDeTemps = []
allSwTemps = []
years = []
# Parse the file and extract data
with open(resultsPath, 'r') as results:
    for line in results:
        #ignore the first line, header
        if 'France' not in line:
            splitLine = line.split(" ")
            allFrTemps.append(int(splitLine[0]))
            allSwTemps.append(int(splitLine[1]))
            allDeTemps.append(int(splitLine[2]))
            years.append(int(splitLine[3]))

# Get the hottest year
frMaxValue = max(allFrTemps)
deMaxValue = max(allDeTemps)
swMaxValue = max(allSwTemps)

maxFrValYear = allFrTemps.index(frMaxValue)
print(maxFrValYear)

# Get the coldest year


#print(allFrTemps,years)