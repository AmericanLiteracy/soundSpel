import sys,csv,operator
fileNameIn = 'SpellReitUnsorted.csv'
fileNameOut = 'SpellReit.csv'

data = csv.reader(open(fileNameIn),delimiter=',')
sortedlist = sorted(data, key=lambda row: str(row[0]).lower())
#now write the sorte result into new CSV file
with open(fileNameOut, "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    prevRow = ''
    for row in sortedlist:
        if row != prevRow:
            fileWriter.writerow(row)
        prevRow = row
