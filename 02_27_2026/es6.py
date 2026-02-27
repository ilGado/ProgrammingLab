#Scrivere un programma che fa la somma di n numeri inseriti dall’utente. 
# Di all'utente di scrivere 0 per fermarsi

def getSumFromInputs():
    
    fromUser = input("Please insert a number (0 to exit): ")
    n = int(fromUser)
    sum = 0
    
    while n != 0:
        
        sum += n
        fromUser = input("Please insert a number (0 to exit): ")
        n = int(fromUser)
        
    return sum

print("Total sum of the numbers inserted: " + str(getSumFromInputs()))

