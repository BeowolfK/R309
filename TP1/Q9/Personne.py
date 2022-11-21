class Personne:
    def __init__(self):
        self.__nom = ""
        self.__prenom = ""
        self.__age = 0
        self.__mail = ""

    def Affiche(self):
        return [self.__nom, self.__prenom, self.__age]

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail):
        self.__mail = mail
