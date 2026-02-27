#Definire una funzione che conta quante vocali sono presenti in una stringa

def countVowel(string): 
    
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    
    for i in vowels:
        
        for j in string:
            
            if i == j:
                counter += 1
                
                
    return counter

string = input("Please insert a string: ")

numVowels = countVowel(string)

print(str(numVowels) + " is the number of vowels in " + string)