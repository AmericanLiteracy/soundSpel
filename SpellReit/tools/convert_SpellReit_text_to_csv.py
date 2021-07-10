fileNameIn = 'soundSpelWurdList.csv'
fileNameOut = 'editedSoundSpelWurdList.csv'

#get file object
fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')
iLine=1
nLinesAltered = 0

while(True):
    #read next lineIn
    lineIn = fileIn.readline()
    #if lineIn is empty, you are done with all lineIns in the file
    if not lineIn:
        break
    # alter line
    nCommas = lineIn.count(',')
    if nCommas !=7:
        #lineOut = lineIn.rstrip('\n') + 'NO_TRANSLATION,!\n'
        #lineOut = lineIn.rstrip(',,,,,,\n') + ',NO_TRANSLATION,!,,,,,\n'
        #fileOut.write(lineIn)
        print('not 7 commas, line:'+str(iLine)+'  '+lineIn)
        nLinesAltered += 1
    else:
        lineOut = lineIn
    # write out line
    #fileOut.write(lineOut)
    iLine+=1

print ('nLinesAltered = ',nLinesAltered)
#close file
fileIn.close
fileOut.close
