import veicolo as v
import auto as a
import moto as m

if __name__ == '__main__':
    veicolo = v.Veicolo("Test1", "Baffo", "1984")
    auto = a.Auto("Aygo", "Toyota", "2009", 5)
    moto = m.Moto("Drz 400 SM", "Suzuki", "2007", "Motard")
    
    print(veicolo)
    print("\n\n")
    print(auto)
    print("\n\n")
    print(moto)
    
    for i in range (0, 5):
        veicolo.accelera()
        
    for(i) in range (0, 3):
        moto.accelera()
        auto.accelera()
        
    auto.frena()
    
    print("\n\n")
    print(veicolo)
    print("\n\n")
    print(auto)
    print("\n\n")
    print(moto)