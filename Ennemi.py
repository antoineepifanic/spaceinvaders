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
        
        # Créer une liste avec les positions initiales des ennemis
        positions_initiales = [60 + n*75 for n in range(8)]
        
        for pos in positions_initiales:
            ennemi = self.canvas.create_image(pos, 50, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        
        self.deplacer_image()

    def deplacer_image(self):
        # Collecter les coordonnées actuelles de tous les ennemis existants
        coords = []
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_all():
                coords.append(self.canvas.coords(ennemi)[0])
        
        # Vérifier s'il y a des ennemis
        if not coords:
            return
        
        # Trouver les positions extrêmes
        minX = min(coords)
        maxX = max(coords)
        
        # Inverser la direction si nécessaire
        if minX <= 35 or maxX >= 635:
            self.dx *= -1
        
        # Déplacer le groupe d'ennemis
        self.canvas.move("groupe", self.dx, 0)
        
        self.fin_de_partie()
        self.missiles(coords)
        
        # Vérifier la collision entre les tirs ennemis et le vaisseau
        for tir_ennemi in self.ennemis_tirs:
            tir_ennemi.CollisionJoueur()
        
        self.canvas.after(100, self.deplacer_image)

    def missiles(self, coords):
        self.fin_de_partie()
        if self.compteur == 15 and coords:
            # Utiliser l'index des coordonnées pour sélectionner un ennemi
            radm = randint(0, len(coords)-1)
            start = coords[radm]
            tir_ennemi = Tir_Ennemi(self.canvas, start, 50)  # 50 est la hauteur initiale des ennemis
            self.ennemis_tirs.append(tir_ennemi)
            self.compteur = 0
        else:
            self.compteur += 1

    def fin_de_partie(self):
        if len(self.ennemis) == 0:
            texte = tk.Label(self.canvas, text="Fin de partie", font=('Helvetica', 30))
            print("Vous avez gagné")
            self.canvas.pack(pady=20)