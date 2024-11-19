# coding: utf-8

class RectangleControle:
    def __init__(self, canvas):
        self.canvas = canvas

        # Créer un rectangle bleu en bas du canevas
        self.rect = self.canvas.create_rectangle(200, 270, 260, 290, fill="blue")

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