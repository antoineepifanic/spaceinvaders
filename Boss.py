# coding: utf-8
""""
import tkinter as tk
from Tir_Ennemi import Tir_Ennemi
from random import randint
from PIL import Image, ImageTk

class Boss:
    def __init__(self, canvas):
        self.canvas = canvas
        self.dx = -3
        # Charger l'image du boss
        self.image = Image.open("ressources/ennemiblanc.png")  # Assurez-vous d'avoir une image spécifique pour le boss
        self.image = self.image.resize((80, 80))  # Taille légèrement plus grande
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Positionner le boss au milieu en largeur, à 50px du haut
        canvas_width = canvas.winfo_width()
        boss_x = canvas_width // 2
        
        # Créer le boss
        self.boss = self.canvas.create_image(boss_x, 50, image=self.photo, tags="boss")
        
        # Compteurs
        self.compteur = 0
        
        # Liste pour stocker les tirs du boss
        self.boss_tirs = []
        
        # Démarrer le mouvement
        self.deplacer_boss()

    def deplacer_boss(self):
        # Déplacer le boss horizontalement
        self.canvas.move("boss", self.dx, 0)
        
        # Récupérer les coordonnées du boss
        coords_boss = self.canvas.coords(self.boss)
        
        # Inverser la direction si nécessaire
        if coords_boss[0] <= 35 or coords_boss[0] >= 635:
            self.dx *= -1
        
        # Tirs aléatoires
        self.missiles()
        
        # Vérifier les collisions des tirs
        for tir in list(self.boss_tirs):
            try:
                tir.CollisionJoueur()
            except Exception:
                self.boss_tirs.remove(tir)
        
        # Continuer le mouvement
        self.canvas.after(100, self.deplacer_boss)

    def missiles(self):
        # Probabilité de tir
        if randint(1, 100) == 1:  # 1% de chance de tirer
            coords_boss = self.canvas.coords(self.boss)
            tir_boss = Tir_Ennemi(self.canvas, self.boss, 0)
            self.boss_tirs.append(tir_boss)