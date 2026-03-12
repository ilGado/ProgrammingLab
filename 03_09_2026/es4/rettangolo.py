import quadrilatero as qdr

class Rettangolo(qdr.Quadrilatero):
    
    def __init__(self, base, altezza):
        
        super().__init__()
        self.base = base
        self.altezza = altezza
        
    def __str__(self):
        return  super().__str__() + f" di base {self.base} e di altezza {self.altezza}"
        
    def perimetro(self):
        return 2*self.altezza + 2*self.base
    
    def area(self):
        return self.base * self.altezza
    
    