fileNameIn = 'soundSpelWurdList.csv'
fileNameOut = 'rearrangedSoundSpelWurdList.csv'

#get file object
fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')
iLine=1

while(True):
    #read next lineIn
    lineIn = fileIn.readline().rstrip('\n')
    #if lineIn is empty, you are done with all lineIns in the file
    if not lineIn:
        break
# 0TS,1soundSpel,2note,3alternatives,4British,5multiple TS,6multiple SS,7long note,8Rondthaler,9pronunciation
# revised:
# 0TS,1soundSpel,2note,8Rondthaler,9pronunciation,7long note,3alternatives,4British,5multiple TS,6multiple SS
    field_list = lineIn.split(',')    # split the line at commas
    lineOut = ','.join((field_list[0],   # rejoin with commas, new order
                        field_list[1],
                        field_list[2],
                        field_list[3],
                        field_list[4],
                        field_list[5],
                        field_list[8],
                        field_list[9],
                        field_list[6],
                        field_list[7]
                           ))+'\n'
    # write out line
    fileOut.write(lineOut)

#close file
fileIn.close
fileOut.close
