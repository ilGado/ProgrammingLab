#menu con opzioni somma, differenza, exit

def menu():
    
    return "- 0 -> EXIT\n- 1 -> a + b\n- 2 -> a - b\n"

if __name__ == "__main__":
    
    print("Benvenuto!")
    
    print(menu())
    check = False
    while not check:
        
        try:
            scelta = int(input("La tua scelta: "))
        except:
            seclta = -1
            
        if scelta == 0:
            check = True
            print("Fine.")
            
        elif scelta == 1:
            
            try:
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"a + b = {a + b}\n")
            except:
                print("Errore: > Devi inserire dei numeri!\n")
        
        elif scelta == 2:
            try:
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"a - b = {a - b}\n")
            except:
                print("Errore: > Devi inserire dei numeri!\n")
        
        else:
            print("Errore: > Devi un valore valido!\n")