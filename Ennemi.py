# coding: utf-8
import tkinter as tk
from Tir_Ennemi import Tir_Ennemi
from random import randint
from PIL import Image, ImageTk

class Ennemi:
    def __init__(self, canvas):
        self.canvas = canvas
        self.dx = -3
        self.image = Image.open("ressources/ennemiblanc.png")
        self.image = self.image.resize((40, 40))
        self.photo = ImageTk.PhotoImage(self.image)
        self.compteur = 0
        self.ennemis = []
        self.ennemis_tirs = []
        for n in range(8):
            ennemi = self.canvas.create_image(60 + n*75, 50, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        self.deplacer_image()

    def deplacer_image(self):
        self.canvas.move("groupe", self.dx, 0)
        coords = []
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_all():
                coords.append(self.canvas.coords(ennemi))
        maxX = 0
        for val in coords:
            if val[0] >= maxX:
                maxX = val[0]
        minX = 600
        for val in coords:
            if val[0] <= minX:
                minX = val[0]
        if minX <= 35 or maxX >= 635:
            self.dx *= -1
        self.fin_de_partie()
        self.missiles(coords)

        # Vérifier la collision entre les tirs ennemis et le vaisseau
        for tir_ennemi in self.ennemis_tirs:
            tir_ennemi.CollisionJoueur()

        self.canvas.after(100, self.deplacer_image)

    def missiles(self, coords):
        self.fin_de_partie()
        if self.compteur == 15 and coords:
            radm = randint(0, len(coords)-1)
            start = coords[radm][0]
            tir_ennemi = Tir_Ennemi(self.canvas, start, coords[radm][1])
            self.ennemis_tirs.append(tir_ennemi)
            self.compteur = 0
        else:
            self.compteur += 1

    def fin_de_partie(self):
        if len(self.ennemis) == 0:
            texte = tk.Label(self.canvas, text="Fin de partie", font=('Helvetica', 30))
            print("Vous avez gagné")
            self.canvas.pack(pady=20)