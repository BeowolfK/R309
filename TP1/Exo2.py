from kivy.app import App
from kivy.uix.label import Label
# from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from verification import isValidEmail, isValidName


class Formulaire(GridLayout):
    def __init__(self, **kwargs):
        super(Formulaire, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2
        self.img = Image(source="assets/rt.png",
                         pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.img)
        self.inside.add_widget(Label(text="Nom : ", font_size="15"))
        self.nom = TextInput(multiline=False, font_size="15")
        self.inside.add_widget(self.nom)
        self.inside.add_widget(Label(text="Prenom : ", font_size="15"))
        self.prenom = TextInput(multiline=False, font_size="15")
        self.inside.add_widget(self.prenom)
        self.inside.add_widget(Label(text="Email : ", font_size="15"))
        self.email = TextInput(multiline=False, font_size="15")
        self.inside.add_widget(self.email)
        self.add_widget(self.inside)
        self.res = Label(text="", font_size="15")
        self.add_widget(self.res)
        self.btnbox = GridLayout()
        self.btnbox.cols = 2
        self.submit = Button(text="envoyer".upper(), font_size="15")
        self.submit.bind(on_press=self.pressed)
        self.btnbox.add_widget(self.submit)
        self.quit = Button(text="quitter".upper(), font_size="15")
        self.quit.bind(on_press=self.quitter)
        self.btnbox.add_widget(self.quit)
        self.add_widget(self.btnbox)

    def quitter(self, instance):
        exit(0)

    def pressed(self, instance):
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


class Exo2(App):
    def build(self):
        self.title = "Formulaire"
        self.icon = "assets/logo.png"
        return Formulaire()


if __name__ == '__main__':
    try:
        Exo2().run()
    except KeyboardInterrupt:
        Exo2().stop()
