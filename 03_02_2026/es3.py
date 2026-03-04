#funzione che prende in input una lista A e due indici, i e j e scambia il contenuto di A[i] e A[j]

import randomArray

def changePositions(array, i, j):   #passa i parametri per riferimento (almeno le liste)
    
    if i != j and i >= 0 and j >= 0 and i <= len(array) and j <= len(array):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        return 1
    
    else: 
        return 0

def dictionary(array):
    
    positions = []
    
    for i in range (0, len(array)):
        positions.append("pos " + str(i))
        
    return {label: value for label, value in zip(positions, array)}


list = randomArray.getRandomList()
toPrint = dictionary(list)

print(f"Original list: {toPrint}")

firstPos = (int(input("Please insert the first position: ")))
secondPos = (int(input("Please insert the second position: ")))

res = changePositions(list, firstPos, secondPos)



if res:
    toPrint = dictionary(list)
    print(f"New list: {toPrint}")
else:
    print("Invalid positions")
