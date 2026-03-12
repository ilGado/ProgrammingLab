
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
    baffo.aggiungiCorso("Analisi 1")
    baffo.rimuoviCorso("Letteratura")
    baffo.saluta()
    
    insegnante.sonoProfessore(baffo.corsi)
    insegnante.sonoProfessore(studente.corsi)
    
    if insegnante.isProf(baffo.corsi):
        print(f"Tutti i corsi di questo studente hanno un docente")
    else: 
        print(f"Non tutti i corsi di questo studente hanno un docente")
        
    if insegnante.isProf(studente.corsi):
        print(f"Tutti i corsi di questo studente hanno un docente")
    else: 
        print(f"Non tutti i corsi di questo studente hanno un docente")