#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from Etudiant import Etudiant
from ClientTCP import ClientTCP
import json


Window.clearcolor = (1, 1, 1, 1)
Window.size = (200, 400)

root = Builder.load_string(
    """
FloatLayout:
    Label:
        text: 'Entrez votre prénom'
        font_size: '16px'
        size_hint: (1 , 0.1)
        pos_hint: {'x': -0.1, 'top': 1}
        color: (0,0,0,1)
        markup: True
    TextInput:
        id: prenom
        multiline: False
        size_hint: (1, .1)
        pos_hint: {'x': 0, 'top': 0.9}

    Label:
        text: 'Entrez votre nom'
        font_size: '16px'
        size_hint: (1 , 0.1)
        pos_hint: {'x': -0.1, 'top': 0.8}
        color: (0,0,0,1)
        markup: True
    TextInput:
        id: nom
        multiline: False
        size_hint: (1, .1)
        pos_hint: {'x': 0, 'top': 0.7}

    Label:
        text: 'Entrez votre eMail'
        font_size: '16px'
        size_hint: (1 , 0.1)
        pos_hint: {'x': -0.1, 'top': 0.6}
        color: (0,0,0,1)
        markup: True
    TextInput:
        id: mail
        multiline: False
        size_hint: (1, .1)
        pos_hint: {'x': 0, 'top': 0.5}

    Label:
        text: '2A'
        font_size: '12px'
        size_hint: (.4,.1)
        pos_hint: {'x':0, 'top': 0.4}
        color: (0,0,0,1)
    CheckBox:
        active: True
        group: "annee"
        on_active: app.get_running_app().edit_annee(2)
        size_hint: (.5,.1)
        pos_hint: {'x':.1, 'top': 0.4}
        canvas.before:
            Color:
                rgb: (.9,.9,.9,1)
            Rectangle:
                pos:self.center_x-8,self.center_y-8
                size:[16,16]
            Color:
                rgb: (.8,.8,.8,1)
            Rectangle:
                pos:self.center_x-7, self.center_y-7
                size:[14,14]
    Label:
        text: '1A'
        font_size: '12px'
        size_hint: (.4,.1)
        pos_hint: {'x':0.4, 'top': 0.4}
        color: (0,0,0,1)
    CheckBox:
        group: "annee"
        on_active: app.get_running_app().edit_annee(1)
        size_hint: (.5,.1)
        pos_hint: {'x':.5, 'top': 0.4}
        canvas.before:
            Color:
                rgb: (.9,.9,.9,1)
            Rectangle:
                pos:self.center_x-8, self.center_y-8
                size:[16,16]
            Color:
                rgb: (.8,.8,.8,1)
            Rectangle:
                pos:self.center_x-7, self.center_y-7
                size:[14,14]
    Label:
        text: 'Entrez votre moyenne'
        font_size: '16px'
        size_hint: (1 , 0.1)
        pos_hint: {'x': -0.1, 'top': 0.35}
        color: (0,0,0,1)
        markup: True
    TextInput:
        id: moyenne
        text: '0'
        multiline: False
        size_hint: (1, .1)
        pos_hint: {'x': 0, 'top': 0.25}
    Button:
        text: 'Enregistrer'
        size_hint: (1 , 0.1)
        pos_hint: {'x': 0, 'top': 0.1}
        border: 10, 10, 10, 10
        on_press: app.get_running_app().register()"""
)


class PersonneInterface(App, Widget):
    def __init__(self):
        super().__init__()
        self.etudiant = Etudiant()
        self.etudiant.annee = "2"
        self.socket = ClientTCP()
        self.sendHTML = True

    def build(self):
        return root

    def register(self):
        self.etudiant.moyenne = int(self.root.ids.moyenne.text)
        self.etudiant.nom = self.root.ids.nom.text
        self.etudiant.prenom = self.root.ids.prenom.text
        self.etudiant.mail = self.root.ids.mail.text
        print(self.etudiant.affiche())

        html = self.create_html()
        if self.sendHTML:
            self.socket.send_etudiant("HTML", html)
        else:
            self.socket.send_etudiant(
                "JSON",
                json.dumps(self.etudiant.affiche_list())
                )

        self.root.ids.moyenne.text = "0"
        self.root.ids.nom.text = ""
        self.root.ids.prenom.text = ""
        self.root.ids.mail.text = ""

        self.etudiant = Etudiant()

    def edit_annee(self, annee):
        self.etudiant.annee = annee

    def create_html(self):
        html = (
            """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        .card {
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
            width: 20%;
            border-radius: 5px;
        }
        .card:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
        img {
            border-radius: 5px 5px 0 0;
        }
        .container {
            padding: 2px 16px;
        }
        </style>
        </head>
        <body>
        <div class="card">
            <img src="../assets/user.png"
            alt="Avatar" style="width:100%">
            <div class="container">
            <h4><b>"""
            + self.etudiant.prenom
            + """ """
            + self.etudiant.nom
            + """</b></h4>
            <h5>"""
            + self.etudiant.mail
            + """</h5>
            <p>"""
            + str(self.etudiant.annee)
            + """A | """
            + str(self.etudiant.moyenne)
            + """ de moyenne</p>
            </div>
        </div>
        </body>
        </html>""")
        return html


PersonneInterface().run()
