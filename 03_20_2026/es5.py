#data in input una data, ritorna i giorni, le ore, i minuti e i secondi al prossimo compleanno da oggi
import datetime

def prossimoCompleanno(comple):
    
    oggi = datetime.datetime.now()

    
    prossimo = datetime.datetime(oggi.year, comple.month, comple.day)
    
    if prossimo <= oggi:
        prossimo = datetime.datetime(oggi.year + 1, comple.month, comple.day)
    
    diff = prossimo - oggi
    
    return diff, oggi, prossimo
    
    


if __name__ == "__main__":
    
    print("Inserisci la tua data di nascita:")
    try:
        gg = int(input("Giorno: "))
        
        if gg <= 0 or gg > 31:
            raise Exception("Errore: > Inserisci un giorno valido")
        
        mm = int(input("Mese: "))
        
        if mm <= 0 or mm > 12:
            raise Exception("Errore: > Inserisci un mese valido")
        
        aa = int(input("Anno: "))
        
        if aa < 1930 or aa > datetime.datetime.now().year:
            raise Exception("Errore: > Inserisci un anno valido")
        
    except ValueError:
        print(f"Errore: > inserisci un numero!")
    
    try:
        compleanno = datetime.date(aa, mm, gg)
    except Exception:
        print("Errore: > Inserisci una data esistente!")
        
        
    print(f"La tua data di nascita: {compleanno.strftime('%d/%m/%Y')}")
    
    tempo, oggi, next = prossimoCompleanno(compleanno)
    
    print(f"Data attuale: {oggi.strftime('%d/%m/%Y, %H:%M:%S')}")
    print(f"Prossimo compleanno: {next.strftime('%d/%m/%Y, %H:%M:%S')}")
    giorni = tempo.days
    ore = tempo.seconds // 3600
    minuti = (tempo.seconds % 3600) // 60
    secondi = tempo.seconds % 60

    print(f"Per festeggiare devi aspettare: {giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi")
    

