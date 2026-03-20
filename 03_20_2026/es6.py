#inserire un numero, se è valido ritorna il quadrato, altrimenti errore e richiede l'input

if __name__ == "__main__":
    
    check = False
    
    while not check: 
        
        try:
            n = int(input("Inserisci un numero: "))
            check = True
        except: 
            print("Devi inserire un numero!")
            check = False
            
    print(f"Il tuo numero: {n}")
    print(f"Il suo quadrato: {n**2}")