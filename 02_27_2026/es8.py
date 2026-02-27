#Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
#triangolo e, se sì, di che tipo di triangolo

def isTriangle(a, b, c):
    
    if a >= b + c or b >= a + c or c >= a + b:
        return 0 #is not a Triangle
    else:
        return 1 #is a Triangle
    

def triangle(a, b, c):
    
    if isTriangle(a, b, c):
        
        #equilateral triangle
        if a == b and b == c:
            return "You've got an equilateral triangle"
        
        #half equilateral triangle
        elif a == 2*b or a == 2*c or b == 2*a or b == 2*c or c == 2*a or c == 2*b:
            return "You've got half equilateral triangle"
        
        #isosceles triangle
        elif a == b or a == c or b == c:
            return "You've got an isosceles triangle"
        
        else:
            return "You've got a scalene triangle"
        
    else:
        return "This is not a triangle!"


aIn = input("Please insert the first side: ")
a = int(aIn)

bIn = input("Please insert the second side: ")
b = int(bIn)

cIn = input("Please insert the third side: ")
c = int(cIn)

print(triangle(a, b, c))