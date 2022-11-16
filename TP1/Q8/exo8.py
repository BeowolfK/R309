class IMC:
    def __init__(self, nom, age, taille, poids):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.poids = poids

    @property
    def imc(self):
        imc = self.poids / (self.taille ** 2)
        return imc

    @property
    def interpretation(self):
        imc = self.imc
        if imc < 16.5:
            return "dénutrition"
        elif 16.5 <= imc < 18.5:
            return "maigreur"
        elif 18.5 <= imc < 25:
            return "corpulence normale"
        elif 25 <= imc < 30:
            return "surpoids"
        elif 30 <= imc < 35:
            return "obésité modérée"
        elif 35 <= imc < 40:
            return "obésité sévère"
        elif imc > 40:
            return "obésité morbide"

    def __str__(self):
        return "Bonjour {}\nVotre IMC est exactement de {}\nVous etes en {}".format(
            self.nom, self.imc, self.interpretation
        )
