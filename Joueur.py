# coding: utf-8
"""
Joueur.py
Gestion du vaisseau du joueur dans le jeu Space Invaders

Ce module gère le comportement du vaisseau du joueur, 
incluant ses déplacements, ses tirs et son système de vie.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

from Tir import Tir
from PIL import Image, ImageTk

class Joueur:
    def __init__(self, canvas):
        """
        Initialise le vaisseau du joueur.

        Args:
            canvas (tk.Canvas): Zone de dessin du jeu
        """
        self.canvas = canvas
        self.image = Image.open("ressources/vaisseau.png")
        self.image = self.image.resize((50, 50))
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = self.canvas.create_image(337, 500, image=self.photo, tags="vaisseau")
        self.dx = 20
        self.vies = 3

        # Liaison des événements de contrôle du vaisseau
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)
        self.canvas.bind_all("<space>", self.tirer)

    def deplacer_gauche(self, event):
        """
        Déplace le vaisseau vers la gauche.

        Args:
            event (tk.Event): Événement de touche du clavier
        """
        coords = self.canvas.coords(self.rect)
        if coords[0] > self.image.width // 2:
            self.canvas.move(self.rect, -self.dx, 0)

    def deplacer_droite(self, event):
        """
        Déplace le vaisseau vers la droite.

        Args:
            event (tk.Event): Événement de touche du clavier
        """
        coords = self.canvas.coords(self.rect)
        if coords[0] < self.canvas.winfo_width() - self.image.width // 2:
            self.canvas.move(self.rect, self.dx, 0)

    def tirer(self, event):
        """
        Tire un missile depuis la position actuelle du vaisseau.

        Args:
            event (tk.Event): Événement de touche du clavier
        """
        coords = self.canvas.coords(self.rect)
        start = coords[0]
        Tir(self.canvas, start)

    def perdre_vie(self):
        """
        Réduit le nombre de vies du joueur.

        Returns:
            bool: True si le joueur n'a plus de vies, False sinon
        """
        self.vies -= 1
        return self.vies == 0