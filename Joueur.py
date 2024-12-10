# coding: utf-8
from Tir import Tir
from PIL import Image, ImageTk

class Joueur:  # on définit le joueur
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = Image.open("ressources/vaisseau.png")
        self.image = self.image.resize((50, 50))  # Redimensionner l'image à une taille plus petite
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = self.canvas.create_image(337, 500, image=self.photo)
        self.dx = 20
        
        # Lier les touches pour le contrôle
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)
        self.canvas.bind_all("<space>", self.tirer)
        
    def deplacer_gauche(self, event):  # les évènements pour le déplacer
        coords = self.canvas.coords(self.rect)
        if coords[0] > self.image.width // 2:
            self.canvas.move(self.rect, -self.dx, 0)
    
    def deplacer_droite(self, event):
        coords = self.canvas.coords(self.rect)
        if coords[0] < self.canvas.winfo_width() - self.image.width // 2:
            self.canvas.move(self.rect, self.dx, 0)
    
    def tirer(self, event):  # l'évènement pour tirer
        coords = self.canvas.coords(self.rect)
        start = coords[0]
        missile = Tir(self.canvas, start)