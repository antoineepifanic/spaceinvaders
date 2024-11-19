# coding: utf-8

import tkinter as tk

class Ennemi:
    def __init__(self, canvas):
        # Garder le canvas
        self.canvas = canvas

        # Charger l'image
        self.image = tk.PhotoImage(file="ressources/ennemi.png")

        self.image = self.image.subsample(9, 12)  

        # Créer un objet image (position initiale)
        self.image_id = self.canvas.create_image(330, 50, image=self.image)

        # Initialiser la direction du mouvement
        self.dx = -5  # Déplacement initial vers la gauche

        # Démarrer l'animation
        self.deplacer_image()

    def deplacer_image(self):
        # Déplacer l'image
        self.canvas.move(self.image_id, self.dx, 0)

        # Récupérer la position actuelle de l'image
        coords = self.canvas.coords(self.image_id)

        # Vérifier si l'image touche les murs
        if coords[0] <= 50 or coords[0] >= 350:
            self.dx = -self.dx  # Inverser la direction

        # Réappeler cette méthode après 20 millisecondes
        self.canvas.after(20, self.deplacer_image)
