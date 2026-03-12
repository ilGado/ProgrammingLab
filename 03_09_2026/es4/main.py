import triangolo
import rettangolo
import poligono
import quadrilatero

if __name__ == "__main__":
    
    p = poligono.Poligono(10)
    print(p)
    
    q = quadrilatero.Quadrilatero()
    print(q)
    
    r = rettangolo.Rettangolo(10, 7)
    print(r)
    print(f"Perimetro: {r.perimetro()}")
    print(f"Area: {r.area()}")
    
    t = triangolo.Triangolo(4, 5, 6)
    print(t)
    print(f"Perimetro: {t.perimetro()}")
    print(f"Equilatero: {t.is_equilatero()}")
    
    tt = triangolo.Triangolo(6, 6, 6)
    print(f"Equilatero: {tt.is_equilatero()}")