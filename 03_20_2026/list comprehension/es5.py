#una lista di interi, una di interi e l'altra di caratteti. 
#crea una lista di coppie (x, y) dove x è pari e l'indice di y è dispari

if __name__ == "__main__":
    
    a = [0, 1, 2, 5, 10, 14, 9, 5, 1, 0, 88, 3, 4]
    b = ["a", "b", "c", "d", "e"]
    
    res = [(x,y) for x in a if x % 2 == 0 for y in b if b.index(y) % 2 != 0]
    
    print(f"A: {a}")
    print(f"B: {b}")
    print(f"RES: {res}")