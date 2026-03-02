#Input una stringa, ritorna true se è palindromo, altrimenti è false

def isPalindromo(string):
    
    inverted = string[::-1]
    
    if string == inverted:
        return 1
    else:
        return 0
    
word = input("Please insert a string: ")

check = isPalindromo(word)

if check:
    print(f"{word} is palindromo")
else:
    print(f"{word} is not palindromo")