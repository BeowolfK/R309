from kivy.app import App
from kivy.uix.label import Label


class PremierProgramme(App):
    def build(self):
        return Label(text="Bonjour, je suis étudiant en R&T", font_size="50")


if __name__ == "__main__":
    try:
        PremierProgramme().run()
    except KeyboardInterrupt:
        PremierProgramme().stop()
