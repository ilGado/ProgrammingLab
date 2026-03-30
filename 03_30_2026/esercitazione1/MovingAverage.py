import ExamException as examExc

class MovingAverage:
    
    def __init__(self, widow_length):
        
        if not isinstance(widow_length, int):
            raise examExc.ExamException("\nErrore: non è un numero intero")
        
        elif widow_length <= 0:
            raise examExc.ExamException("\nErrore: la finestra deve essere un numero strettamente positivo")
                    
        else:
            self.widow_length = widow_length  
        
    def computate(self, lista):
        
        
        if isinstance(lista, list): #lista è un vettore
            
            if self.widow_length <= len(lista): #la lunghezza di lista è >= di quella della finestra
            
                if all(isinstance(item, (int, float)) for item in lista):  #la lista è di numeri
                    toReturn = []
                    counter = 0
                    tmpSum = 0
        
                    for x in lista:
            
                        tmpSum += x
                        counter += 1
            
                        if counter == self.widow_length:
                
                            toReturn.append(tmpSum / self.widow_length)
                            tmpSum -= lista[len(toReturn) - 1]
                            counter -= 1
        
                    return toReturn
                else:   #la lista non ha solo numeri
                    raise examExc.ExamException("\n Errore: non è una lista di numeri")
            
            else: #la lunghezza di lista è < di quella della finestra
                raise examExc.ExamException("\n Errore: la lunghezza della lista è minore di quella della finestra")
        
        else:   #lista non è un vettore
            raise examExc.ExamException("\nErrore: non è una lista")
                
                
        
        