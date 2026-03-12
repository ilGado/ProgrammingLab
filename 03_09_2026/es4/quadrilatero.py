import poligono as plgn

class Quadrilatero(plgn.Poligono):
    
    def __init__(self):
        super().__init__(4)
        
    def __str__(self):
        return f"Sono un Quadrilatero"