# Convert from one spelling system to another
'''
usage: 
python convert_html.py input.html output.html
where input.html is the original in standard spelling,
and output.html is in reform spelling.  
Create input.html by saving a page from your web
browser.  View output.html by openning that file
from disk in your web browser.
In addition, this script must have access to the 
file DIAMBG, a dictionary of American (reform) 
spelling, in the run directory.
Mark Petersen
August 2016
'''

import sys
import pickle
import time

# load dictionary:
fileName = 'dictionaries/soundSpel.pickle'
ss = pickle.load( open( fileName, 'rb' ) )

# if len(sys.argv)<3:
#     print "input and output files required"
#     sys.exit()
    
################################################
#
#  Read in text file to translate
#
################################################

# f = open(sys.argv[1], 'r')
# x = f.read()
# f.close()

#x = 'one two three four I love you too, though through the thicken I may judge you'
x = input('Type text to translate and hit return:\n')

################################################
#
#  Translate text
#
################################################

# x is input, y is output, just like in highschool algebra.
# Initialize y as an empty list.
y=[]
i=0
# Iterate over all characters in input string
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
            reformWord = ss[word]
 
            # Keep upper case the same as the original
            if x[iBeg:i].istitle():
                y.append( reformWord.title() )
            elif x[iBeg:i].isupper():
                y.append( reformWord.upper() )
            else:
                y.append( reformWord )

        # If word is not found in the dictionary, take it
        # verbatim.
        except:
            y.append( x[iBeg:i] )

    # If the character is not a letter, take it directly.
    else:
        y.append( x[i] )
        i+=1

################################################
#
#  Save translated text as new file
#
################################################
print('\nTranslation:\n')
print(''.join(y))

# f = open(sys.argv[2], 'w')
# f.write(''.join(y))
# f.close()
