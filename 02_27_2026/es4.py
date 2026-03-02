#Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte 
#quella lettera è contenuta nella parola

def countCharacter(word, charac):
    
    counter = 0
    
    for x in word.upper():
        if x == charac.upper():
            counter += 1
            
    return counter

word = input("Please insert a word: ")
charac = input("Please insert a character: ")

res = countCharacter(word, charac)

print("The character '" + charac + "' is repeated " + str(res) + " times in '" + word + "'")