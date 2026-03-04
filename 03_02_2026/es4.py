#Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un elemento in comune

import randomArray

def isInArr(a1, a2):
    
    toReturn = 0 #False
    
    for element1 in a1:
        
        for element2 in a2:
            
            if element1 == element2:
                toReturn = 1 #True: at least one element is in both arrays
                break
    
    return toReturn

array1 = randomArray.getRandomList()
array2 = randomArray.getRandomList()

print(f"First array: {array1}")
print(f"Second array: {array2}")


res = isInArr(array1, array2)

if res:
    print("These two arrays have at least one element in common")
else:
    print("These two arrays don't have any element in common")