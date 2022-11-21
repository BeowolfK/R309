class Voiture:
    def __init__(self, marque, modele, volumeCarburant, distanceParcouru):
        self.marque = marque
        self.modele = modele
        self.volumeCarburant = volumeCarburant
        self.distanceParcouru = distanceParcouru

    def get_Data(self, marque, modele, volumeCarburant, distanceParcouru):
        self.marque = marque
        self.modele = modele
        self.volumeCarburant = volumeCarburant
        self.distanceParcouru = distanceParcouru

    @property
    def consoEur(self):
        return round(100 / self.distanceParcouru * self.volumeCarburant, 2)

    @property
    def consoUsa(self):
        return round(
            (self.distanceParcouru / 1.609) / (self.volumeCarburant / 3.785), 2
        )
