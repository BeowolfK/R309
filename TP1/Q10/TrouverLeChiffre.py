#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

import sys
import random


Window.size = (200, 300)
Window.clearcolor = (1, 1, 1, 1)

Config.set("graphics", "width", "200")
Config.set("graphics", "height", "300")
Config.set("graphics", "resizable", "0")

root = Builder.load_string(
    """
FloatLayout:
    Image:
        source: "../assets/number.png"
        allow_stretch: True
        keep_ratio: False
        size_hint_x: 1
        size_hint_y: 0.33
        pos_hint: {'left': 1, 'top': 1}
    Label:
        id: txt
        text: 'Trouver le chiffre 0-10'
        font_size: '16px'
        size_hint: (1 , 0.1)
        pos_hint: {'left': 1, 'top': 0.65}
        color: (0,0,0,1)
        markup: True
    TextInput:
        id: vol
        multiline: False
        size_hint: (1, .1)
        pos_hint: {'x': 0, 'top': 0.3}
    Button:
        text: 'Valider'
        size_hint: (1 , 0.1)
        pos_hint: {'left': 1, 'top': 0.2}
        on_press: app.get_running_app().check()
    Button:
        text: 'Quitter'
        size_hint: (1 , 0.1)
        pos_hint: {'left': 1, 'top': 0.1}
        on_press: app.get_running_app().quitter()
"""
)


class Number(App, Widget):
    def build(self):
        self.num = random.randint(0, 10)
        return root

    def check(self):
        if self.root.ids.vol.text.replace(" ", "") != "":
            try:
                nb = int(self.root.ids.vol.text)
                if nb == self.num:
                    self.root.ids.txt.text = "[b][color=#11ff00]Bravo ![/color][/b]"
                elif nb < self.num:
                    self.root.ids.txt.text = "[color=#ff2a00]Trop bas[/color]"
                elif nb > self.num:
                    self.root.ids.txt.text = "[color=#ff2a00]Trop haut[/color]"
                self.root.ids.vol.text = ""
            except ValueError:
                self.root.ids.txt.text = "[color=#ff2a00]Erreur[/color]"

    def afficher(self):
        pass

    def quitter(self):
        sys.exit()


Number().run()
