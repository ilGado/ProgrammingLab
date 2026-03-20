import random

def getRandomList(size = None, max = None):
    
    toReturn = []
    
    if size == None:
        size = random.randint(1, 25)
        
    if max == None:
        max = 100
        
    for x in range (0, size):
        toReturn.append(random.randint(1,max))
        
    return toReturn

