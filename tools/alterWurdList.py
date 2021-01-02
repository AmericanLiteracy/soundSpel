fileNameIn = 'soundSpelWurdList.csv'
fileNameOut = 'editedSoundSpelWurdList.csv'

#get file object
fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')
nLinesAltered = 0

while(True):
    #read next lineIn
    lineIn = fileIn.readline()
    #if lineIn is empty, you are done with all lineIns in the file
    if not lineIn:
        break
    # alter line
    nCommas = lineIn.count(',')
    if nCommas == 6:
        #lineOut = lineIn.rstrip('\n') + 'NO_TRANSLATION,!\n'
        lineOut = lineIn.rstrip(',,,,,,\n') + ',NO_TRANSLATION,!,,,,,\n'
        #fileOut.write(lineIn)
        nLinesAltered += 1
    else:
        lineOut = lineIn
    # write out line
    fileOut.write(lineOut)

print ('nLinesAltered = ',nLinesAltered)
#close file
fileIn.close
fileOut.close
