# coding: utf-8

import tkinter as tk
from Joueur import Joueur
from Ennemi import Ennemi

class RectangleControle:
    def __init__(self, canvas):
        self.canvas = canvas

        # Créer un rectangle bleu en bas du canevas
        self.rect = self.canvas.create_rectangle(200, 170, 260, 190, fill="blue")

        # Taille du déplacement
        self.dx = 20

        # Lier les touches pour le contrôle
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)

    def deplacer_gauche(self, event):
        # Récupérer les coordonnées actuelles
        coords = self.canvas.coords(self.rect)

        # Vérifier les bords (ne pas dépasser le bord gauche)
        if coords[0] > 0:
            self.canvas.move(self.rect, -self.dx, 0)

    def deplacer_droite(self, event):
        # Récupérer les coordonnées actuelles
        coords = self.canvas.coords(self.rect)

        # Vérifier les bords (ne pas dépasser le bord droit)
        if coords[2] < self.canvas.winfo_width():
            self.canvas.move(self.rect, self.dx, 0)

def obtenir_score():
    return 69  # Faudra changer mdr pour une fonction qui donne le vrai score

def demarrer_partie():
    canevas = tk.Canvas(fenetrejeu, width=500, height=400, bg="black")
    canevas.pack()
    global rectangle_controle
    rectangle_controle = Joueur(canvas_partie)

def record():
    return 100

if __name__ == "__main__":
    # Créer la fenêtre principale uniquement si ce fichier est exécuté directement
    fenetre = tk.Tk()
    fenetre.title("Animation de l'image rebondissante")

    # Créer une instance de l'animation
    animation = Ennemi(fenetre)
    fenetre.mainloop()