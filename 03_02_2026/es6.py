#Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il
#conteggio delle occorrenze.


def setWords():
    
    toReturn = []
    
    fromUser = input("Please insert any words you want one for time (type \"quit\" to stop): ")
    
    while(fromUser != "quit"):
        
        toReturn.append(fromUser)
        fromUser = input("Please insert any words you want one for time (type \"quit\" to stop): ")
    
    return toReturn

def countOccurrences(arr):
    
    toReturn = []
    
    for i in arr: #cycling every element in array
        
        counter = 0
        
        for j in arr: #for each letter counts how many times it appears
            
            if i == j:
                counter += 1
        
        toReturn.append(counter)
        
    return toReturn

def setDictionary(arrSrc, arrCounts):
    
    return {label: value for label, value in zip(arrSrc, arrCounts)} #KEYS: arrSrc (string), #VALUES: arrCounts (int)

words = setWords()

print(f"Your words: {words}")

occurrences = countOccurrences(words)
dic = setDictionary(words, occurrences)

print(f"{dic}")


