import veicolo as v

class Auto(v.Veicolo):
    
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
        
    def __str__(self):
        return f"Marca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\nNumero porte: {self.numero_porte}\nVelocita' attuale: {self.speed}"
    
    def accelera(self):
        super().accelera()
        
    def frena(self):
        super().frena()