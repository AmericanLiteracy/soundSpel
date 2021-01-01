fileNameIn = 'soundSpelWurdList.csv'
fileNameOut = 'editedSoundSpelWurdList.csv'
#get file object
fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')

while(True):
    #read next lineIn
    lineIn = fileIn.readline()
    #if lineIn is empty, you are done with all lineIns in the file
    if not lineIn:
        break
    # alter line
    lineOut = lineIn
    # write out line
    fileOut.write(lineOut)

#close file
fileIn.close
fileOut.close
