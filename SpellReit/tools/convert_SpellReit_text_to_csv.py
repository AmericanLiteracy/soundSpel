fileNameIn = 'old_versions/spell_reit_list.txt'
#fileNameIn = 'spell_reit_sample.txt'
fileNameOut = 'SpellReitUnsorted.csv'

#get file object
fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')

while(True):
    lineIn1 = fileIn.readline()
    #print('lineIn1: ',lineIn1.strip())
    if lineIn1=='\n':
        #print( 'len(lineIn1)==new line ')
        continue
    if len(lineIn1)==2:
        #print( 'len(lineIn1)==single character ')
        continue
    #if lineIn is empty, you are done with all lineIns in the file
    if not lineIn1:
        break

    lineIn2 = fileIn.readline()
    if lineIn2=='\n':
        continue
    #print('lineIn2: ',lineIn2.strip())
    lineOut = lineIn1.strip().split(' ')[0].replace("’","'") + ',' + lineIn2.replace("’","'")
    #print('lineOut: ',lineOut.strip())
    fileOut.write(lineOut)

#close file
fileIn.close
fileOut.close
