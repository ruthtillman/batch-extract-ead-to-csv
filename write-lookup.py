import os, csv, pickle

# Comment these out to initialize the first time.
lookupFile = open('/Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/lookup.py', 'r')
lookup = pickle.load(lookupFile)
lookupFile.close()

def writeLookup(PIDAndFile, lookup):
    savedLookup = open('/Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/lookup.py','w')
    openFile = open(PIDAndFile)
    workingCSV = csv.reader(openFile)
    for row in workingCSV:
        lookup[row[0]] = row[1]
    pickle.dump(lookup,savedLookup)

PIDAndFile = raw_input("Path to the file with successfully-ingested PID and filenames: ")
writeLookup(PIDAndFile, lookup)
print "There are", len(lookup), "items in lookup"
