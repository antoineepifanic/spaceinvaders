import tkinter as tk

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

def record():
    return 100

import tkinter as tk

class Animation:
    def __init__(self, fenetre):
        # Créer un canvas
        self.canvas = tk.Canvas(fenetre, width=400, height=300, bg="lightblue")
        self.canvas.pack(expand=True)

        # Créer un rectangle (position initiale)
        self.rect = self.canvas.create_rectangle(330, 50, 370, 70, fill="green")

        # Initialiser la direction du mouvement
        self.dx = -5  # Déplacement initial vers la gauche

        # Démarrer l'animation
        self.deplacer_rectangle()

    def deplacer_rectangle(self):
        # Déplacer le rectangle
        self.canvas.move(self.rect, self.dx, 0)

        # Récupérer la position actuelle du rectangle
        coords = self.canvas.coords(self.rect)

        # Vérifier si le rectangle touche les murs
        if coords[0] <= 0 or coords[2] >= 400:
            self.dx = -self.dx  # Inverser la direction

        # Réappeler cette méthode après 20 millisecondes
        self.canvas.after(20, self.deplacer_rectangle)

if __name__ == "__main__":
    # Créer la fenêtre principale uniquement si ce fichier est exécuté directement
    fenetre = tk.Tk()
    fenetre.title("Animation du rectangle rebondissant")

    # Créer une instance de l'animation
    animation = Animation(fenetre)
    fenetre.mainloop()


