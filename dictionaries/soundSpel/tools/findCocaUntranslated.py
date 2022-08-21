'''
Find words in Cocos dictionary that are not translated to soundSpel
See https://docs.google.com/spreadsheets/d/1xk8jnP30QClKVPQVG6qb1amDb1RDD7atHM4Cd1sTJnQ

Run with python tools/findCocosUntranslated.py
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

coca = pd.read_csv('../coca_100k_word_frequency/b1386_head60k.txt',delim_whitespace=True,encoding_errors='ignore')
cocaCol = coca.columns
ss = pd.read_csv('soundSpel.csv',low_memory=False)
ssCol = ss.columns

cocaID = coca['ID']
cocaWord = coca['w1']
cocaRoot = coca['L1']
# Frequency (per million words) in the 450 million word Corpus of Contemporary American English (http://corpus.byu.edu/coca)
cocaFreqPerMil = coca['coca'] 
ssWordTO = ss['TO']
ssWord = ss['SS']
# using dictionary comprehension to convert lists to dictionary
ssDict = {ssWordTO[i]: ssWord[i] for i in range(len(ssWordTO))}

cocaWordSS = []
cocaWordNotFound = []
cocaWordNotFoundss = []
cocaWordNotFoundBlank = []
cocaRootNotFound = []
cocaIDNotFound = []
cocaFreqNotFound = []
for i in range(19001,len(cocaWord)):
# skip hyphenated word
    if cocaWord[i].find('-')>-1:
        print('i,w1',i,cocaWord[i])
        continue
    try:
        cocaWordSS.append(ssDict[cocaWord[i]])
    except:
        ssString = 'notfound'+str(int(round(cocaID[i]/1000)))+'k'
        cocaWordSS.append(ssString)
        cocaWordNotFound.append(cocaWord[i])
        cocaWordNotFoundss.append(ssString)
        cocaWordNotFoundBlank.append('')
        if cocaRoot[i]==cocaWord[i]:
            cocaRootNotFound.append('')
        else:
            cocaRootNotFound.append(cocaRoot[i])
        cocaIDNotFound.append(cocaID[i])
        if cocaFreqPerMil[i] > 10*cocaFreqPerMil[i-1]:
            cocaFreqNotFound.append(cocaFreqPerMil[i-1])
        else:
            cocaFreqNotFound.append(cocaFreqPerMil[i])

df = pd.DataFrame()
df['TO']  = cocaWordNotFound
df['SS'] = cocaWordNotFoundBlank
df['freq rank']  = cocaIDNotFound
df['freq per Mil']  = cocaFreqNotFound
df['root if differs']  = cocaRootNotFound
df.to_csv('workdir/coca_ordered_missing_soundSpel_20k.csv', index=False, header=True)

#df = pd.DataFrame()
#df['cocaOrder']  = cocaID
#df['cocaWord']  = cocaWord
#df['soundSpel'] = cocaWordSS
#df['cocaRoot']  = cocaRoot
#df['cocaFreqPerMil']  = cocaFreqPerMil
#df.to_csv('workdir/coca_ordered_soundSpel_20k.csv', index=False)
## grep NOT --color=never coca_ordered_soundSpel_20k.csv> not_in_soundSpel.csv
#
