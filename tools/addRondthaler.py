import pickle
import pandas as pd

fileName = 'old_versions/DIAMBG.pickle'
fileNameIn = 'soundSpelWurdList.csv'
fileNameIn = 'sample.csv'
fileNameOut = 'addRondthalerSoundSpelWurdList.csv'

#get file object
RondthalerDict = pickle.load( open( fileName, 'rb' ) )
df = pd.read_csv(fileNameIn, dtype=str, na_filter=False)
ssDict = dict(zip(df.TS,df.soundSpel))
df.insert(4, 'SSmatchRond', 'NA', allow_duplicates=True)

for idx,row in df.iterrows():
    print (idx,row['TS'])
    if row['TS'] in RondthalerDict:
       df.at[idx,'Rondthaler'] = RondthalerDict[row['TS']]
       if df.at[idx,'soundSpel'] == RondthalerDict[row['TS']]:
           df.at[idx,'SSmatchRond'] = 'T'
       else:
           df.at[idx,'SSmatchRond'] = 'F'
    else:
       print('did not find: ',row['TS'])




#fileIn = open(fileNameIn, 'r')
#fileOut = open(fileNameOut, 'w')
#
#iLine=1
#while(True):
#    #read next lineIn
#    lineIn = fileIn.readline().rstrip('\n')
#    if not lineIn:
#        break
## 0TS,1soundSpel,2note,Rondthaler,RondthalerSame
#    field_list = lineIn.split(',')    # split the line at commas
#    lineOut = ','.join((field_list[0],   # rejoin with commas, new order
#                        field_list[1],
#                        field_list[2],
#                        field_list[3],
#                        field_list[4],
#                        field_list[5],
#                        field_list[8],
#                        field_list[9],
#                        field_list[6],
#                        field_list[7]
#                           ))+'\n'
#    # write out line
#    fileOut.write(lineOut)
#
##close file
#fileIn.close
#fileOut.close
