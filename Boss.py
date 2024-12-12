"""
Boss.py
Gestion de l'ennemi bonus du jeu Space Invaders

Ce module gère le comportement de l'ennemi bonus qui apparaît périodiquement
et traverse l'écran de gauche à droite, offrant des points bonus au joueur.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

import tkinter as tk
from PIL import Image, ImageTk

class Ennemi_bonus:
    def __init__(self, canvas):
        """
        Initialise l'ennemi bonus

        Args:
            canvas: La zone de jeu où l'ennemi sera affiché
        """
        self.canvas = canvas
        self.dx = 10  # Vitesse de déplacement horizontal
        
        # Configuration de l'apparence
        self.image = Image.open("ressources/ennemivert.png")
        self.image = self.image.resize((25, 25))
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Création de l'ennemi bonus hors écran
        self.boss = self.canvas.create_image(-30, 290, image=self.photo, tags="boss")
        
        self.deplacer()
    
    def deplacer(self):
        """
        Gère le déplacement de l'ennemi bonus
        Il traverse l'écran de gauche à droite puis disparaît
        """
        coords = self.canvas.coords(self.boss)
        canvas_width = self.canvas.winfo_width()
        
        # Continue le déplacement tant que l'ennemi n'est pas sorti de l'écran
        if coords[0] < canvas_width + 30:  # +30 pour sortir complètement
            self.canvas.move(self.boss, self.dx, 0)
            self.canvas.after(50, self.deplacer)
        else:
            # Suppression une fois sorti de l'écran
            self.canvas.delete(self.boss)