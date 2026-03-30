
import CSVTimeSeriesFile as csvReader
import ExamException as examExc

def get_lists(list):
    
    values = []
    years = []
    counter = 0
    
    for elem in list:
        
        year = elem[0].split("-")[0]
        
        if not year in years: #anno non ancora preso in considerazione
            
            years.append(year) 
            values.append([]) #aggiungo la lista dei valori per quell'anno
            
            
            #valori di controllo: partono da 0 e False perché non ho ancora mai trovato almeno una data nell'elenco contente l'anno estratto in precedenza
            check = False
            visited = 0
            
            for item in list: #scorro nuovamente la lista
        
                if year in item[0]:  #ho trovato il mio anno: so che i dati sono in sequenza quindi scorro finchè ho valori per quell'anno
                    visited = 1
                    check = True
                    values[counter].append(item[1])
                else:   
                    check = False
                    
                if check == False and visited == 1: #ho finito la sequenza e sono sicuro di averla vista tutta
                    break
        
            counter += 1   #prossima lista di values sarà in questa posizione
            
    return years, values

def calc_mean(lists):
    
    toReturn = []
    
    for list in lists:
        
        sum = 0
        elements = 0
        
        for el in list:
            
            try:
                sum += int(el)
                elements += 1
            except:
                pass
        
        toReturn.append(round(sum/elements, 1))


    return toReturn

def computate_variations(time_series, first_year, last_year):
    if int(first_year) < int(last_year):
        
        years, values = get_lists(time_series)
        means = calc_mean(values)
    
    
        if first_year in years and last_year in years:
            
            dictKey = first_year + "-" + last_year
            dictVal = means[years.index(last_year)] - means[years.index(first_year)]
            print(means[years.index(last_year)])
            print(means[years.index(first_year)])
            return {dictKey : dictVal} #KEYS: dictKey (string), #VALUES: dictVal (int)
        
        else:
            raise examExc.ExamException("Errore: anni non trovati")
    
    else:
        raise examExc.ExamException("Errore: il primo anno deve essere minore del secondo")
    


if __name__ == "__main__":
    
    tmp = csvReader.CSVTimeSeriesFile("data.csv")
    
    data = tmp.get_data()
    
    res = computate_variations(data, "1949", "1955")
    
    print(res)
    
    
    
    # years, values = get_lists(data)
    # means = calc_mean(values)
    # print(f"Years: {years}\nVal: {values}") #test
    # print(means) #test
    