class IMC:
    def __init__(self, taille, poids):
        self.taille = taille
        self.poids = poids

    @property
    def imc(self):
        imc = self.poids / (self.taille ** 2)
        return round(imc, 2)

    @property
    def interpretation(self):
        imc = self.imc
        if imc < 18.5:
            return "maigre"
        elif 18.5 <= imc < 25:
            return "normal"
        elif 25 <= imc < 30:
            return "en surpoids"
        elif imc > 30:
            return "obèse"
