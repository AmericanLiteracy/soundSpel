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
cocaFreqPerMil = coca['pcoca'] 
ssWordTO = ss['TO']
ssWord = ss['SS']
# using dictionary comprehension
# to convert lists to dictionary
ssDict = {ssWordTO[i]: ssWord[i] for i in range(len(ssWordTO))}

cocaWordSS = []
cocaWordNotFound = []
for i in range(len(cocaWord)):
    try:
        cocaWordSS.append(ssDict[cocaWord[i]])
    except:
        cocaWordSS.append('NOT_FOUND')

df = pd.DataFrame()
df['cocaOrder']  = cocaID
df['cocaWord']  = cocaWord
df['soundSpel'] = cocaWordSS
df['cocaRoot']  = cocaRoot
df['cocaFreqPerMil']  = cocaFreqPerMil
df.to_csv('workdir/coca_ordered_soundSpel_20k.csv', index=False)

