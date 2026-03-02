#Scrivere una funzione che sommi tutti gli elementi di una lista

import random

def getSum(list):
    
    sum = 0
    
    for number in list:
        sum += number
        
    return sum

def getRandomList():
    
    toReturn = []
    
    size = random.randint(1, 25)
    
    for x in range (0, size):
        toReturn.append(random.randint(1,100))
        
    return toReturn

list = getRandomList()
sum = getSum(list)

print(f"List: {list}")
print(f"Sum: {sum}")
