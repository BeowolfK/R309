from Personne import Personne


class Etudiant(Personne):
    def __init__(self):
        super().__init__()
        self.__annee = 0
        self.__matiere = ""
        self.__moyenne = 0.0

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee):
        self.__annee = annee

    @property
    def matiere(self):
        return self.__matiere

    @matiere.setter
    def matiere(self, matiere):
        self.__matiere = matiere

    def affiche(self):
        return [
            super().nom,
            super().prenom,
            super().age,
            self.__annee,
            self.__matiere,
            self.__moyenne,
        ]
