from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from voiture import Voiture

Window.size = (900, 500)


class Consommation(Widget):
    # eu: eu
    # usa: usa
    # res: res
    # marque: marque
    # modele: modele
    # distance: distance
    # vol: vol
    eu = ObjectProperty(None)
    usa = ObjectProperty(None)
    res = ObjectProperty(None)
    marque = ObjectProperty(None)
    modele = ObjectProperty(None)
    distance = ObjectProperty(None)
    vol = ObjectProperty(None)

    def submit(self):
        try:
            v = Voiture(
                self.marque.text,
                self.modele.text,
                float(self.distance.text),
                float(self.vol.text),
            )
            if self.eu.state == "down":
                self.res.text = f"{v.consoEur}L/100km"
            elif self.usa.state == "down":
                self.res.text = f"{v.consoUsa}gallons per miles"
            else:
                self.res.text = "Erreur"
        except ValueError as err:
            print(err)
            self.res.text = "Erreur"

    def quit(self):
        exit(0)


class voitureApp(App):
    def build(self):
        return Consommation()


if __name__ == "__main__":
    voitureApp().run()
