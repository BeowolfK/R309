from banque import CompteBancaire
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Window.size = (900, 700)


class Formulaire(Widget):
    pass

    res = ObjectProperty(None)
    nom = ObjectProperty(None)
    numCompte = ObjectProperty(None)
    montant = ObjectProperty(None)
    solde = ObjectProperty(None)
    header = ObjectProperty(None)
    solde_result = ObjectProperty(None)
    action = ObjectProperty(None)
    c = CompteBancaire()

    def new_account(self):
        try:
            self.c.solde = float(self.solde.text)
            self.c.numeroCompte = int(self.numCompte.text)
            self.c.nom = self.nom.text
            self.res.text = "Compte créé"
            self.solde_result.text = self.c.afficher()

        except ValueError as err:
            print(err)
            print(self.solde.text)
            print(self.numCompte.text)
            print(self.nom.text)
            self.res.text = "Compte non créé"

    def debit(self):
        try:
            if self.action.text == "Déposer":
                self.c.versement(int(self.montant.text))
                self.solde_result.text = self.c.afficher()
                self.res.text = "Dépôt effectué"
            elif self.action.text == "Retirer":
                self.c.retrait(int(self.montant.text))
                self.solde_result.text = self.c.afficher()
                self.res.text = "Retrait effectué"
            else:
                self.res.text = "Erreur"
        except ValueError as err:
            print(err)
            self.res.text = "Erreur, action non enregistré"

    def quit(self):
        exit(0)


class banqueApp(App):
    def build(self):
        self.title = "Banque"
        self.icon = "../assets/logo.png"
        return Formulaire()


if __name__ == "__main__":
    banqueApp().run()
