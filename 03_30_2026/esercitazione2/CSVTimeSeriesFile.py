import csv
import ExamException as examExc
import os

class CSVTimeSeriesFile:
    
    def __init__(self, name):
        self.name = name
        self.dir = "03_30_2026/esercitazione2/"
        self.file = self.dir + self.name
        
    def get_data(self):
        
        if os.path.exists(self.file) and os.path.isfile(self.file):     #esiste il file nella working directory
            try:
                with open(self.dir + self.name, newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    
                    toReturn = []
                    
                    counter = 0
                    for row in reader:
                        
                        if counter == 0:
                            counter += 1
                        else:
                            
                            for data in toReturn:
                                
                                if row[0] in data[0]:
                                    raise examExc.ExamException("Errore: linea duplicata")
                            
                            toReturn.append(row)    
                        
                                
                
                    return toReturn
            except IOError:
                print("Errore: impossibile aprire il file")
             
        else:  #non esiste il file nella working directory

            raise examExc.ExamException("Errore: non è stato trovato questo file")