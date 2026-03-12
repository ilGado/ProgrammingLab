import persona as ps

class Studente(ps.Persona):
    
    def __init__(self, nome, cognome, corsi = None):
        super().__init__("Studente UNITS", nome, cognome)
        if corsi == None:
            self.corsi = []
        else:
            self.corsi = corsi
        
    def saluta(self):
        ps.Persona.saluta(self)
        print(f"> Frequento i corsi: {self.corsi}")
        
    def aggiungiCorso(self, toAdd):
        self.corsi.append(toAdd)
        print(f"Aggiunto il corso {toAdd}")
        
    def rimuoviCorso(self, toRem):
        
        if toRem in self.corsi:
            self.corsi.remove(toRem)
            print(f"Rimosso il corso {toRem}")
            
        else:
            print(f"Non frequenti il corso {toRem}")