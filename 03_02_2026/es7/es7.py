#Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file
#passato come argomento
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

def getColumns(path):
    
    file = fromFile.readFile(path)
    
    names = []
    sales = []
    prices= []
    
    for row in file:
        names.append(row["nome_shampoo"])
        sales.append(row["vendite_totali"])
        prices.append(row["prezzo_unitario"])
        
    return names, sales, prices

def countSales(path):
    
    names, sales, prices = getColumns(path)
    sum = 0
    for item in sales:
        sum += int(item)
        
    return sum
    
path = os.path.join(base_dir, "shampoo_vendite.csv")
res = countSales(path)
print(f"Total sales: {res}")

