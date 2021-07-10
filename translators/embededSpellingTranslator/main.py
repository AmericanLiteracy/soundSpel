# Translates from traditional spelling to another system
# Mark Petersen, American Literacy Council
# May 2021

import csv
import string as str

dictionary = {}
with open('dictionary.csv', encoding='UTF-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      dictionary[row[0]] = row[1]

def soundSpel(x):
  y=[]
  i=0
                
  while i< len(x):
    iBeg = i

    # Check for beginning of html declaration.
    # If found, take the declaration verbatim
    if x[i]=='<':
      while x[i]!='>':
        i+=1
      i+=1
      y.append( x[iBeg:i] )

    # Check for beginning of a word.  Advance the
    # index until the whole word is found.
    elif x[i].isalpha():
      while x[i].isalpha():
        i+=1
        if i==len(x):
          break
      word = x[iBeg:i].lower()

      # Translate word to reform spelling.
      try:
        reformWord = dictionary[word]

        # Keep upper case the same as the original
        if x[iBeg:i].istitle():
          reformWord = reformWord.title()
        elif x[iBeg:i].isupper():
          reformWord = reformWord.upper()
        
        if reformWord.lower() == word.lower():
          # unaltered word: Color yellow
          reformWord = '\x1b[0;96m' + reformWord + '\x1b[0m'
        else:
          # altered word: color blue
          reformWord = '\x1b[0;93m' + reformWord + '\x1b[0m'

        y.append( reformWord )

      # If word is not found in the dictionary, take it
      # verbatim.
      except:
        y.append( '\x1b[0;31m' + x[iBeg:i] + '\x1b[0m' )
        #y.append( x[iBeg:i] )

    # If the character is not a letter, take it directly.
    else:
      y.append( x[i] )
      i+=1
  return ''.join(y)

print("Colors indicate \x1b[0;96munaltered\x1b[0m, \x1b[0;93maltered\x1b[0m, \x1b[0;31mnot in dictionary\x1b[0m")
print("\x1b[0;96mType or paste your text, press enter. You can enter multiple lines.\x1b[0m")
while True:
  x = input()
  print(soundSpel(x))

