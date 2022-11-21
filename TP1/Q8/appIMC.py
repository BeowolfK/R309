from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from exo8 import IMC


Window.size = (500, 500)
Window.clearcolor = (1, 1, 1, 1)


class MainWindow(Widget):
    nom = ObjectProperty(None)
    poids = ObjectProperty(None)
    taille = ObjectProperty(None)
    res = ObjectProperty(None)
    res_img = ObjectProperty(None)

    def get_imc(self):
        try:
            imc_rep = IMC(float(self.taille.text), float(self.poids.text))
            if imc_rep.imc < 18.5:
                self.res.text = f"{self.nom.text.title()}, vous êtes maigre !\nVous avez un IMC de {imc_rep.imc}"
                self.res_img.source = "../assets/maigre.png"
            elif 18.5 <= imc_rep.imc < 25:
                self.res.text = f"{self.nom.text.title()}, vous êtes normal !\nVous avez un IMC de {imc_rep.imc}"
                self.res_img.source = "../assets/normal.png"
            elif 25 <= imc_rep.imc < 30:
                self.res.text = f"{self.nom.text.title()}, vous êtes en surpoids !\nVous avez un IMC de {imc_rep.imc}"
                self.res_img.source = "../assets/surpoids.png"
            elif imc_rep.imc > 30:
                self.res.text = f"{self.nom.text.title()}, vous êtes obèse !\nVous avez un IMC de {imc_rep.imc}"
                self.res_img.source = "../assets/obese.png"
        except ValueError:
            self.res.text = f"Il doit y avoir une erreur quelque part :/ !"
            self.res_img.source = "../assets/error.png"


kv = Builder.load_file("new_window.kv")


class exo8App(App):
    def build(self):
        self.title = "IMC"
        self.icon = "../assets/logo.png"
        return MainWindow()


if __name__ == "__main__":
    exo8App().run()
