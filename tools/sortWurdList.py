import sys,csv,operator
fileNameIn = 'soundSpelWurdList.csv'
fileNameOut = 'sortedSoundSpelWurdList.csv'

data = csv.reader(open(fileNameIn),delimiter=',')
sortedlist = sorted(data, key=lambda row: str(row[0]).lower())
#now write the sorte result into new CSV file
with open(fileNameOut, "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        #print(row)
        fileWriter.writerow(row)
