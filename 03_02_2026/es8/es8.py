#Definire una funzione che prende in input un file ed una parola e conta quante volte
#quella parola è presente sul file
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

def searchWord(toSearch, path):

    text = fromFile.getFile(path) #strings of chars
    words = text.replace(",", " ").replace(";", " ").replace(".", " ").split() #default are blank spaces, words is an array of words
    
    counter = 0
    
    for word in words:
        if word.lower() == toSearch.lower():
            counter += 1
            
    return counter


word = input("Please insert a word you want to search in a file: ")
path = os.path.join(base_dir, "words.txt")
res = searchWord(word, path)

print(f"Times {word} appeared: {res}")