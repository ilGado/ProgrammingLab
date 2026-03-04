#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una
#lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] -
#>["uno","zero","sette","nove","otto"] 

import randomArray

def setDictionary():
    
    numbers = []
    
    for i in range (0,10):
        numbers.append(i)
        
    names = ["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
    
    return {label: value for label, value in zip(numbers, names)} #KEYS: numbers (int), VALUES: names (string)


def getNumberNames(arr, dic):
    
    toReturn = []
    
    for num in arr: #cycling every number in arr
        
        toReturn.append(dic[num])
        
    return toReturn
            
dictionary = setDictionary()
array = randomArray.getRandomFirstNumbers()
array_words = getNumberNames(array, dictionary)

print(f"Array with numbers: {array}")
print(f"Array with number names: {array_words}")
