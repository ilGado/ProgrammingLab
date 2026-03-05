#Definire una funzione conteggio che prende come input un file e ritorna un dizionario
#con chiave le parole e valore il numero di volte che la parola è presente nel file.


import sys
import os

# cartella dello script corrente (es9)
current_dir = os.path.dirname(__file__)  

# cartella del progetto (una sopra)
project_dir = os.path.abspath(os.path.join(current_dir, ".."))  # .. = cartella superiore

# aggiungi la cartella del progetto al path
sys.path.append(project_dir)

import fromFile


base_dir = os.path.dirname(__file__)  

def getDictionary(path):
    
    file = fromFile.getFile(path)
    words = file.replace(",", " ").replace(";", " ").replace(".", " ").split()
    
    counting = []
    
    for toCount in words:
        
        counter = 0
        for word in words:
            
            if word.lower() == toCount.lower():
                counter += 1
                
        counting.append(counter)
        
    return {label: value for label, value in zip(words, counting)} #KEYS: words (string), #VALUES: counting (int)

def printDic(dic):
    
    print("Dictionary: ")
    
    for key, value in dic.items():
        
        print(f"\"{key.lower()}\": {value}")

path = os.path.join(base_dir, "words.txt")
dic = getDictionary(path)
printDic(dic)
