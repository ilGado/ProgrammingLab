class Canguro:
    
    def __init__(self, list = None):               #non __init__(self, list = []) e poi assegnare a self.__list = list[], altrimenti ogni oggetto avrà l'attributo list chr punta ALLA STESSA LISTA!
        if list is None:
            self.__contenuto_tasca = []
        else:
            self.__contenuto_tasca = list
        
    def intasca(self, item):
        self.__contenuto_tasca.append(item)
        
    def __str__(self):
        return f"{self.__contenuto_tasca}"