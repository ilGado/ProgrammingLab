
import csv

def getFile(path):
    
    my_file = open(path, 'r')
    toReturn = my_file.read()
    my_file.close()
    return toReturn

def readFile(file):
    
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)