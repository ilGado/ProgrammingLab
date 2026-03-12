import veicolo as v

class Moto(v.Veicolo):
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo
        
    def __str__(self):
        return f"Marca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\nTipo: {self.tipo}\nVelocita' attuale: {self.speed}"
    
    
    def accelera(self):
        super().accelera()
        
    def frena(self):
        super().frena()