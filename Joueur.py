# coding: utf-8
from Tir import Tir

class Joueur:
    def __init__(self, canvas):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(200, 370, 260, 390, fill="blue")
        self.dx = 20

        # Lier les touches pour le contrôle
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)
        self.canvas.bind_all("<space>", self.tirer)

    def deplacer_gauche(self, event):
        coords = self.canvas.coords(self.rect)
        if coords[0] > 0:
            self.canvas.move(self.rect, -self.dx, 0)

    def deplacer_droite(self, event):
        coords = self.canvas.coords(self.rect)
        if coords[2] < self.canvas.winfo_width():
            self.canvas.move(self.rect, self.dx, 0)
    
    def tirer (self, event) :
        coords = self.canvas.coords(self.rect)
        start = (coords[0] + coords [2])/2
        missile =Tir(self.canvas, start)
        

