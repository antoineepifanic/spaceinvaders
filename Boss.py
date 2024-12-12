# coding: utf-8
import tkinter as tk
from PIL import Image, ImageTk

class Ennemi_bonus:
    def __init__(self, canvas):
        self.canvas = canvas
        self.dx = 10  # Vitesse de déplacement horizontal triplée (était 5)
        
        # Chargement de l'image
        self.image = Image.open("ressources/ennemivert.png")
        self.image = self.image.resize((25, 25))  # Plus petit que les ennemis normaux
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Création du boss hors écran à gauche
        self.boss = self.canvas.create_image(-30, 290, image=self.photo, tags="boss")
        
        # Démarrer le mouvement
        self.deplacer()
    
    def deplacer(self):
        # Obtenir les coordonnées actuelles
        coords = self.canvas.coords(self.boss)
        canvas_width = self.canvas.winfo_width()
        
        # Si encore visible à l'écran, continuer le déplacement
        if coords[0] < canvas_width + 30:  # +30 pour sortir complètement de l'écran
            self.canvas.move(self.boss, self.dx, 0)
            self.canvas.after(50, self.deplacer)
        else:
            # Une fois sorti de l'écran, supprimer le boss
            self.canvas.delete(self.boss)