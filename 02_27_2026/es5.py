#Scrivere un programma che verifica se un numero inserito dall’utente è primo

def isPrime(n):
    
    if n == 1 or n == 0:
        return 1
    
    for i in range (2,n):
        
        if n % i == 0:
            return 0
        
    
    return 1
        
number = input("Please insert a number: ")

n = int(number) 

res = isPrime(n)

if res:
    print(number + " is prime")
else:
    print(number + " is not prime")