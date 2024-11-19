import tkinter as tk

def obtenir_score():
    return 69  # Faudra changer mdr pour une fonction qui donne le vrai score

def demarrer_partie():
    canevas = tk.Canvas(fenetrejeu, width=500, height=400, bg="black")
    canevas.pack()

def record():
    return 100

import tkinter as tk

import tkinter as tk

class Animation:
    def __init__(self, fenetre):
        # Créer un canvas
        self.canvas = tk.Canvas(fenetre, width=400, height=300, bg="lightblue")
        self.canvas.pack(expand=True)

        # Charger l'image
        self.image = tk.PhotoImage(file="/Users/antoineepifanic/spaceinvaders-4/ressources/ennemi.png")

        self.image = self.image.subsample(6, 8)  

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

if __name__ == "__main__":
    # Créer la fenêtre principale uniquement si ce fichier est exécuté directement
    fenetre = tk.Tk()
    fenetre.title("Animation de l'image rebondissante")

    # Créer une instance de l'animation
    animation = Animation(fenetre)
    fenetre.mainloop()