from enum import Enum

class Geschlecht(Enum):
    Male = 1
    Female = 2

class Firma:
    def __init__(self, name, mitarbeiter=[], abteilungen=[], personen=[], gruppenleiter=[]):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.abteilungen = abteilungen
        self.personen = personen
        self.gruppenleiter = gruppenleiter
    
    def getAnzMitarbeiter(self):
        return len(self.mitarbeiter)
    
    def getAnzGruppenleiter(self):
        return len(self.gruppenleiter)
    
    def getAnzAbteilungen(self):
        return len(self.abteilungen)
    
    def getAnzPersonen(self):
        return len(self.personen)

    def printAbteilungen(self):
        for x in self.abteilungen:
            print(f"{x.name} - {x.description}")
    
    def getStrongestAbteilung(self):
        abt = self.abteilungen
        return max(abt)

class Person:
    def __init__(self, name, abteilung, geschlecht):
        self.name = name
        self.abteilung = abteilung
        self.geschlecht = geschlecht

class Mitarbeiter(Person):
    def __init__(self, name, abteilung, geschlecht, gehalt):
        super().__init__(name, abteilung, geschlecht)
        self.gehalt = gehalt       

class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, abteilung, geschlecht, gehalt, gruppe):
        super().__init__(name, abteilung, geschlecht, gehalt)
        self.gruppe = gruppe

class Abteilung:
    def __init__(self, name, description, personen=[]):
        self.name = name
        self.description = description
        self.personen = personen
    
    def addPerson(self, person):
        self.personen.append(person)
    
    def run(self):
        print("Machen Abteilungs Zeug")

    def __str__(self):
        return f"{self.name} - {self.description} - Personen Anz.: {len(self.personen)}"

class Buchhaltung(Abteilung):
    def __init__(self, name, description, personen=[]):
        super().__init__(name, description, personen)

    def run(self):
        print("Buchhalten...")


class Produktion(Abteilung):
    def __init__(self, name, description, personen=[]):
        super().__init__(name, description, personen)   

    def run(self):
        print("Herstellen v. Produkt")

def main():
    personen = []
    for i in range(5):
        personen.append(Person(f'Person{i}', Abteilung, Geschlecht.Male))
    
    abteilung = Abteilung("Wirtschaft", "Wirtschafting in se unternehmen", personen)

    abteilung1 = Buchhaltung("Buchhaltung", "Haltung des Buches", personen=[Person('Buchhalter', Abteilung, Geschlecht.Male)])


    firma = Firma("Nimmersatt", personen=personen, abteilungen=[abteilung, abteilung1])

    print(f"Anzahl Abteilung: {firma.getAnzAbteilungen()}")
    print(f"Anzahl Gruppenleiter: {firma.getAnzGruppenleiter()}")
    print(f"Anzahl Mitarbeiter: {firma.getAnzMitarbeiter()}")
    print(f"Anzahl Personen: {firma.getAnzPersonen()}")
    firma.printAbteilungen()
    print(firma.getStrongestAbteilung().__str__())
    

if __name__ == "__main__":
    main()