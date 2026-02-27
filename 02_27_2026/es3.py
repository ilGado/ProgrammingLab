#Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari

def isOdd(n):
    return n % 2

number = input("Please insert a number: ")

n = int(number)

res = isOdd(n)

if res:
    print(str(n) + " is odd")
else:
    print(str(n) + " is even")