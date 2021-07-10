import pickle

fileNameIn = 'old_versions/DIAMBG'
fileNameOut = 'old_versions/DIAMBG.pickle'

# Open file of entries for American (reform) spelling.
f = open(fileNameIn, 'r')
rawString = f.read()
f.close()

# Create a python dictionary relating each
# standard word and it's reform version
a = rawString.split()
RondthalerDict = {}
for i in range(int(len(a)/2)):
    RondthalerDict[a[2*i]] = a[2*i+1]

pickle.dump(RondthalerDict, open( fileNameOut, 'wb' ) )
