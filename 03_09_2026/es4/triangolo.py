import poligono as plgn

class Triangolo(plgn.Poligono):
    
    def __init__(self, lato1, lato2, lato3):
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
        
    def __str__(self):
        return super().__str__() + f" di lati: {self.lato1}, {self.lato2}, {self.lato3}"
    
    def perimetro(self):
        return self.lato3 + self.lato2 + self.lato1
    
    def is_equilatero(self):
        return self.lato1 == self.lato2 and self.lato2 == self.lato3
            