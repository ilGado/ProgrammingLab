import csvfile as csv
import numericalcsvfile as ncsv

import sys
import os

# cartella dello script corrente (es9)
current_dir = os.path.dirname(__file__)  

# cartella del progetto (una sopra)
project_dir = os.path.abspath(os.path.join(current_dir, ".."))  # .. = cartella superiore

# aggiungi la cartella del progetto al path
sys.path.append(project_dir)

base_dir = os.path.dirname(__file__) 
name = "shampoo_vendite.csv"
path = os.path.join(base_dir, name)

if __name__ == '__main__':
    
    
    
    file = csv.CSVFile(path, name, " ")
    try:
        with open(path) as f: 
            file.write(f.readlines())
            #a = file.getData("AquaSilk Shampoo Variante 10,3548,11.36", "AquaSilk Shampoo Variante 12,1670,10.61")
            a = file.getData(2, 5)
            for el in a:
                print(el)
    except FileNotFoundError:
        print(f"{path} does not exist!")
    
    # file = ncsv.NumericalCSVFile(path, name, " ")
    # try:
    #     with open(path) as f: 
    #         file.write(f)
    #         #file.getData()
    #         a = file.getData()

    #         for el in a:
    #             print(el)
            
    # except FileNotFoundError:
    #     print(f"{path} does not exist!")