import os

class CSVFile:
    
    def __init__(self, path,  name, content):
        
        if os.path.exists(path):    
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
        
        
    def getData(self):
        if self.path != None:
            toReturn = []
            
            for line in self.content:
                
                toReturn.append(line.replace("\n", "").split(','))
                
            
            return toReturn
        else:
            return f"File given is not valid!"
    
    
        