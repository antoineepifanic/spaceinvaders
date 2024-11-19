# coding: utf-8

import tkinter as tk
from Joueur import Joueur
from Ennemi import Ennemi

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