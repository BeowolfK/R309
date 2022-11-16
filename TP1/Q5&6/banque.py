class CompteBancaire:
    def __init__(self):
        self.__numeroCompte = 0
        self.__nom = ""
        self.__solde = 0

    @property
    def numeroCompte(self):
        return self.__numeroCompte

    @numeroCompte.setter
    def numeroCompte(self, numeroCompte):
        self.__numeroCompte = numeroCompte

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def solde(self):
        return round(self.__solde, 2)

    @solde.setter
    def solde(self, solde):
        self.__solde = solde

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde - montant < 0:
            if self.__solde < 0:
                self.agios(montant)
            else:
                temp = montant - self.__solde
                self.__solde = 0
                self.agios(temp)

        else:
            self.__solde -= montant

    def agios(self, montant):
        self.__solde -= montant * 1.05

    def afficher(self):
        return (
            "numero : "
            + str(self.__numeroCompte)
            + "\nnom : "
            + self.__nom
            + "\nsolde : "
            + str(round(self.__solde, 2))
            + "€"
        )
