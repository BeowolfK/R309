from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Window.size = (500, 500)
Window.clearcolor = (1, 1, 1, 1)


class maigreWindow(Widget):
    pass


class normalWindow(Widget):
    pass


class surpoidsWindow(Widget):
    pass


class obeseWindow(Widget):
    pass


class MainWindow(Widget):
    nom = ObjectProperty(None)
    age = ObjectProperty(None)
    poids = ObjectProperty(None)
    taille = ObjectProperty(None)
    
    def submit(self):
        show_popup("Vous etes obèse", obeseWindow())
        print("ok")


kv = Builder.load_file('new_window.kv')


class exo8App(App):
    def build(self):
        self.title = "IMC"
        self.icon = "../assets/logo.png"
        return MainWindow()


def show_popup(title, show):
    popup = Popup(title=title, content=show, size_hint=(None, None), size=(400, 400))
    popup.open()


if __name__ == "__main__":
    exo8App().run()
