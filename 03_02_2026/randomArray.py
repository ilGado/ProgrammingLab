import random

def getRandomList():
    
    toReturn = []
    
    size = random.randint(1, 25)
    
    for x in range (0, size):
        toReturn.append(random.randint(1,100))
        
    return toReturn

def getRandomFirstNumbers():
    
    toReturn = []
    
    size = random.randint(1, 25)
    
    for x in range (0, size):
        toReturn.append(random.randint(0,9)) #i due estermi inclusi, per non far includere l'ultimo si usa random.randrange(x,y)
        
    return toReturn