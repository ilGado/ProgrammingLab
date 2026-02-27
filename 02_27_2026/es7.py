#Definire la funzione fattoriale (versione iterativa)

def factorial(n):
    
    res = 1
    
    for i in range(2,n+1):
        res *= i
        
    return res

fromUser = input("Please insert a number: ")

n = int(fromUser)

fac = factorial(n)

print(fromUser + "! = " + str(fac))