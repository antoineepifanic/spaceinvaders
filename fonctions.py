# coding: utf-8
import tkinter as tk
from Joueur import Joueur
from Ennemi import Ennemi

class RectangleControle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(200, 170, 260, 190, fill="blue")
        self.dx = 20
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)

    def deplacer_gauche(self, event):
        coords = self.canvas.coords(self.rect)
        if coords[0] > 0:
            self.canvas.move(self.rect, -self.dx, 0)

    def deplacer_droite(self, event):
        coords = self.canvas.coords(self.rect)
        if coords[2] < self.canvas.winfo_width():
            self.canvas.move(self.rect, self.dx, 0)

def obtenir_score():
    return 0

def record():
    try:
        with open("record.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        with open("record.txt", "w") as f:
            f.write("0")
        return 0

def sauvegarder_record(nouveau_score):
    ancien_record = record()
    if nouveau_score > ancien_record:
        with open("record.txt", "w") as f:
            f.write(str(nouveau_score))

def demarrer_partie():
    canevas = tk.Canvas(fenetrejeu, width=500, height=400, bg="black")
    canevas.pack()
    global rectangle_controle
    rectangle_controle = Joueur(canvas_partie)

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Animation de l'image rebondissante")
    animation = Ennemi(fenetre)
    fenetre.mainloop()