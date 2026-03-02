#Scrivere un programma che chiede all’utente un numero intero e stampa il suo quadrato e il suo cubo

def getSquare(n):
    return n**2

def getCube(n):
    return n**3


number = input("Please insert a number: ")

n = int(number)

square = getSquare(n)
cube = getCube(n)

print("Your number: " + str(n) + "\nIts square: " + str(square) + "\nIts cube: " + str(cube))


