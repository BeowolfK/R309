from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from verification import isValidEmail, isValidName


Window.size = (700, 700)


class Formulaire(Widget):
    nom = ObjectProperty(None)
    prenom = ObjectProperty(None)
    email = ObjectProperty(None)
    res = ObjectProperty(None)

    def quit(self):
        exit(0)

    def submit(self):
        nom = self.nom.text
        prenom = self.prenom.text
        email = self.email.text
        if nom == "" or not isValidName(nom):
            self.res.text = "Nom invalide"
        elif prenom == "" or not isValidName(prenom):
            self.res.text = "Prénom invalide"
        elif email == "" or not isValidEmail(email):
            self.res.text = "Email invalide"
        else:
            print(f"Nom : {nom}\nPrenom : {prenom}\nMail : {email}")
            self.res.text = f"Nom : {nom}\nPrenom : {prenom}\nMail : {email}"


class exo4App(App):
    def build(self):
        self.title = "Formulaire"
        self.icon = "../assets/logo.png"
        return Formulaire()


if __name__ == "__main__":
    exo4App().run()
