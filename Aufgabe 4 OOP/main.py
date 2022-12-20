from enum import Enum

class Gender(Enum):
    Male = 1
    Female = 2

class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender)
        self.firma = firma


class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender, firma)


class Firma():
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def compare_men_women(self):
        anz_male = 0
        anz_female = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.gender == Gender.Female:
                    anz_female += 1
                    continue
                anz_male += 1

            for gruppenleiter in abteilung.gruppenleiter:
                if gruppenleiter.gender == "women":
                    anz_female += 1
                    continue
                anz_male += 1
        return {Gender.Male.name: anz_male, Gender.Female.name: anz_female}

    def anz_abteilung(self):
        return len(self.abteilungen)

    def anz_mitarbeiter(self):
        count = 0
        for abteilung in self.abteilungen:
            count += len(abteilung.mitarbeiter)
        return count

    def anz_gruppenleiter(self):
        count = 0
        for abteilung in self.abteilungen:
            count+= len(abteilung.gruppenleiter)
        return count

    def get_biggest_abteilung(self):
        biggest_abteilung = self.abteilungen[0]
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > len(biggest_abteilung.mitarbeiter):
                biggest_abteilung = abteilung
        return biggest_abteilung

class Abteilung():
    def __init__(self, name, gruppenleiter):
        self.name = name
        self.gruppenleiter = []
        self.gruppenleiter.append(gruppenleiter)
        self.mitarbeiter = []


def main():
    firma = Firma("Gucci")
    abteilung = Abteilung("GucciWerbung", Gruppenleiter("AV", Gender.Male, firma))
    firma.abteilungen.append(abteilung)
    abteilung2 = Abteilung("GucciProduktion", Gruppenleiter("AV", Gender.Male, firma))
    firma.abteilungen.append(abteilung2)

    abteilung.gruppenleiter.append(Mitarbeiter("Boss", Gender.Male, firma))
    abteilung.mitarbeiter.append(Mitarbeiter("nedsoboss", Gender.Male, firma))
    abteilung.mitarbeiter.append(Mitarbeiter("nedsoboss", Gender.Male, firma))
    abteilung.mitarbeiter.append(Mitarbeiter("nedsoboss", Gender.Male, firma))
    
    

if __name__ == "__main__":
    main()