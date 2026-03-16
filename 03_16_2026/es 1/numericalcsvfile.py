import csvfile as csv

class NumericalCSVFile(csv.CSVFile):
    
    def __init__(self, path,  name, content):
        super().__init__(path, name, content)
        
    def write(self, toAdd):
        super().write(toAdd)
        
    def getData(self):
        list = super().getData()
        
        try:
            toReturn = []
            for line in list:
                i = 0
                toAdd = []
                for element in line:
                    if i != 0:
                        try:
                            tmp = float(element)
                            #print(f"\nSiamo qui: {tmp}")
                            toAdd.append(tmp)
                            
                        except:
                            print(f"\n - {element} impossible to convert from str to float")
                            toAdd.append(element)
                    else:
                        toAdd.append(element)
                    i += 1
                toReturn.append(toAdd)
                    
            return toReturn
        except: 
            return "Invalid list!"