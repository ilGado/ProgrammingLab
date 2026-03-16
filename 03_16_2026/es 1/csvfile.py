import os

class CSVFile:
    
    def __init__(self, path,  name, content):
        
        if isinstance(path, str) and os.path.exists(path):    
            self.path = path
            self.name = name
            self.content = content
        else:
            self.path = None
            self.name = None
            self.content = None
            
        
        
    def write(self, toAdd):
        if self.content != None:
            self.content = toAdd
        
    
    def getData(self, start=None, end=None):
        if self.path is None:
            return "File given is not valid!"

        toReturn = []

        try:
            for i in range(start, end + 1):
                line = self.content[i]   # qui scatta IndexError se fuori range
                toReturn.append(line.strip().split(','))

        except Exception:
            for line in self.content:
                toReturn.append(line.strip().split(','))

        return toReturn
    
    
        