'''
Find words in Cocos dictionary that are not translated to soundSpel

Run with tools/findCocosUntranslatd.py
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

coca = pd.read_csv('../coca_100k_word_frequency/b1386_head20k.txt',delim_whitespace=True,encoding_errors='ignore')
cocaCol = coca.columns
ss = pd.read_csv('soundSpel.csv')
ssCol = ss.columns

cocaID = coca['ID']
cocaWord = coca['w1']
cocaRoot = coca['L1']
# Frequency (per million words) in the 450 million word Corpus of Contemporary American English (http://corpus.byu.edu/coca)
cocaFreqPerMil = coca['coca'] 
ssWordTO = ss['TO']
ssWord = ss['SS']
# using dictionary comprehension
# to convert lists to dictionary
ssDict = {ssWordTO[i]: ssWord[i] for i in range(len(ssWordTO))}

cocaWordSS = []
cocaWordNotFound = []
cocaWordNotFoundss = []
cocaWordNotFoundBlank = []
cocaRootNotFound = []
cocaIDNotFound = []
cocaFreqNotFound = []
for i in range(len(cocaWord)):
    try:
        cocaWordSS.append(ssDict[cocaWord[i]])
    except:
        ssString = 'notfound'+str(int(round(cocaID[i]/1000)))+'k'
        cocaWordSS.append(ssString)
        cocaWordNotFound.append(cocaWord[i])
        cocaWordNotFoundss.append(ssString)
        cocaWordNotFoundBlank.append('')
        cocaRootNotFound.append(cocaRoot[i])
        cocaIDNotFound.append(cocaID[i])
        cocaFreqNotFound.append(cocaFreqPerMil[i])


df = pd.DataFrame()
df['TO']  = cocaWordNotFound
df['SS'] = cocaWordNotFoundBlank
df['root']  = cocaRootNotFound
df['freq rank']  = cocaIDNotFound
df['freq per Mil']  = cocaFreqNotFound
df.to_csv('workdir/coca_ordered_missing_soundSpel_20k.csv', index=False, header=True)

df = pd.DataFrame()
df['cocaWordNotFound']  = cocaWordNotFound
df['cocaWordNotFoundss']  = cocaWordNotFoundss
df.to_csv('workdir/coca_ordered_not_found_20k.csv', index=False)

df = pd.DataFrame()
df['cocaOrder']  = cocaID
df['cocaWord']  = cocaWord
df['soundSpel'] = cocaWordSS
df['cocaRoot']  = cocaRoot
df['cocaFreqPerMil']  = cocaFreqPerMil
df.to_csv('workdir/coca_ordered_soundSpel_20k.csv', index=False)
# grep NOT --color=never coca_ordered_soundSpel_20k.csv> not_in_soundSpel.csv

