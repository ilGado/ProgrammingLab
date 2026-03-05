#Definire una funzione che prende come input un file, rimuove tutte le righe duplicate,
#scrive il risultato in un nuovo file chiamato unique.txt.


import os

base_dir = os.path.dirname(__file__)  


def getFile(path):
    
    toReturn = open(path, 'r')
    return toReturn

def getLines(file):
    
    toReturn = []
    
    for line in file:
        
        line = line.strip() #to remove \n and strange spaces
        
        if not line in toReturn:
            toReturn.append(line)
            
    return toReturn

def writeOnFile(lines):
    
    name = "unique.txt"

    if os.path.exists(name):
        toWrite = open(name, 'w')
    else:
        toWrite = open(name, 'x')
        
        
    for line in lines:
        toWrite.write(line + "\n")
        
    toWrite.close()

def toExecute():
    
    path = os.path.join(base_dir, "text.txt")
    file = getFile(path)

    lines = getLines(file)
    file.close()
    
    writeOnFile(lines)

toExecute()