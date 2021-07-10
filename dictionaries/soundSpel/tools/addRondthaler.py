import pickle
import pandas as pd

fileName = 'old_versions/DIAMBG.pickle'
fileNameIn = 'soundSpelWurdList.csv'
#fileNameIn = 'sample.csv'
fileNameOut = 'addRondthalerSoundSpelWurdList.csv'

RondthalerDict = pickle.load( open( fileName, 'rb' ) )
df = pd.read_csv(fileNameIn, dtype=str, na_filter=False)
ssDict = dict(zip(df.TS,df.soundSpel))
df.insert(4, 'SSmatchRond', 'NA', allow_duplicates=True)

for idx,row in df.iterrows():
    #print (idx,row['TS'])
    if row['TS'] in RondthalerDict:
       df.at[idx,'Rondthaler'] = RondthalerDict[row['TS']]
       if df.at[idx,'soundSpel'] == RondthalerDict[row['TS']]:
           df.at[idx,'SSmatchRond'] = 'T'
       else:
           df.at[idx,'SSmatchRond'] = 'F'
    else:
       pass 
       #print('did not find: ',row['TS'])

df.to_csv(fileNameOut,index=False)
