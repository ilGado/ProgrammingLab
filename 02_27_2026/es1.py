#Stampa 538 min nel formato 8h:58min

def getTime(n):
    
    hours = 0
     
    while n >= 60:
        n -= 60
        hours += 1
        
    return hours, n

h, m = getTime(538)

print("Time: " + str(h) +"h:" + str(m) + "min")

