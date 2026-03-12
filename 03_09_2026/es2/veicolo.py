class Veicolo:
    
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
        
    def __str__(self):
        return f"Marca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\nVelocita' attuale: {self.speed}"
    
    def accelera(self):
        self.speed += 5
        
    def frena(self):
        self.speed -= 5
        
    def getSpeed(self):
        return self.speed