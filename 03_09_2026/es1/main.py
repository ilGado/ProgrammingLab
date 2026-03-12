
import docente as dc
import studente as sd

if __name__ == "__main__":
    
    
    insegnante = dc.Docente("Daniele", "Del Santo", ["Analisi 1", "Analisi 2"])
    studente = sd.Studente("Irene", "Rossi", ["Programmazione", "Laboratorio", "Analisi", "Geometria"])
    baffo = sd.Studente("baffo", "baffone")
    
    insegnante.saluta()
    studente.saluta()
    baffo.saluta()
    
    insegnante.rimuoviCorso("Analisi 2")
    insegnante.saluta()
    baffo.aggiungiCorso("Geometria")
    baffo.rimuoviCorso("Letteratura")
    baffo.saluta()
    