import persona as ps

class Docente(ps.Persona):
    
    def __init__(self, nome, cognome, corsi = None):
        super().__init__("Docente UNITS", nome, cognome)
        if corsi == None:
            self.corsi = []
        else:
            self.corsi = corsi
        
    def saluta(self):
        ps.Persona.saluta(self)
        print(f"> Docente dei corsi: {self.corsi}")
        
    def aggiungiCorso(self, toAdd):
        self.corsi.append(toAdd)
        print(f"Aggiunto il corso {toAdd}")
        
    def rimuoviCorso(self, toRem):
        
        if toRem in self.corsi:
            self.corsi.remove(toRem)
            print(f"Rimosso il corso {toRem}")
            
        else:
            print(f"Non frequenti il corso {toRem}")
            
    def isProf(self, list):
        
        check = True
        
        for corso in list:
            
            if corso not in self.corsi:
                
                check = False
                break
            
        return check
        
    def sonoProfessore(self, list):
        
        check = self.isProf(list)
        
        if check:
            print(f"{self.nome} {self.cognome} insegna tutti i corsi di questo studente")
            
        else:
            print(f"{self.nome} {self.cognome} non insegna tutti i corsi di questo studente")