class Persona:
    
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo,
        self.nome = nome,
        self.cognome = cognome
        
    def saluta(self):
        print(f"Ciao sono {self.ruolo}, {self.nome} {self.cognome}")
        