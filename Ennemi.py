"""
Ennemi.py
Gestion des ennemis standards du jeu Space Invaders

Ce module gère le comportement des ennemis standards : leur création,
déplacement, tirs et détection des conditions de fin de partie.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

import tkinter as tk
from Tir_Ennemi import Tir_Ennemi
from random import randint
from PIL import Image, ImageTk
from Boss import Ennemi_bonus 

class Ennemi:
    def __init__(self, canvas):
        """
        Initialise le groupe d'ennemis
        
        Args:
            canvas: La zone de jeu où les ennemis seront affichés
        """
        self.canvas = canvas
        self.dx = -3  # Vitesse de déplacement horizontal
        self.image = Image.open("ressources/ennemiblanc.png")
        self.image = self.image.resize((40, 40))
        self.photo = ImageTk.PhotoImage(self.image)
        self.compteur = 0
        self.descente_compteur = 0
        self.apparition_bonus = 0
        self.ennemis = []
        self.ennemis_tirs = []
        self.limite_y = 400  # Position Y maximale avant game over
        
        # Création de la première rangée d'ennemis
        for n in range(8):
            ennemi = self.canvas.create_image(60 + n*75, 50, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        
        # Création de la deuxième rangée
        for n in range(8):
            ennemi = self.canvas.create_image(60 + n*75, 100, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        
        self.deplacer_image()

    def deplacer_image(self):
        """Gère le déplacement du groupe d'ennemis et leurs actions"""
        if not self.ennemis:
            return
        
        self.canvas.move("groupe", self.dx, 0)
        
        # Vérification de la position Y maximale des ennemis
        max_y = 0
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                y = self.canvas.coords(ennemi)[1]
                if y > max_y:
                    max_y = y
        
        # Game over si les ennemis descendent trop bas
        if max_y >= self.limite_y:
            fenetre = self.canvas.winfo_toplevel()
            fenetre.game_over()
            return
        
        # Collecte des coordonnées pour le rebond sur les bords
        coords = []
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                coords.append(self.canvas.coords(ennemi)[0])
        
        if not coords:
            return
        
        # Gestion des rebonds sur les bords
        minX = min(coords)
        maxX = max(coords)
        
        if minX <= 35 or maxX >= 635:
            self.dx *= -1
        
        self.missiles(coords)
        
        # Gestion des tirs ennemis
        for tir_ennemi in list(self.ennemis_tirs):
            try:
                tir_ennemi.CollisionJoueur()
            except Exception:
                self.ennemis_tirs.remove(tir_ennemi)
        
        # Gestion des compteurs
        self.descente_compteur += 1
        self.apparition_bonus += 1
        
        # Descente périodique des ennemis
        if self.descente_compteur >= 30:
            self.canvas.move("groupe", 0, 20)
            self.descente_compteur = 0
        
        # Apparition de l'ennemi bonus
        if self.apparition_bonus == 160:
            self.apparition_bonus = 0
            self.boss = Ennemi_bonus(self.canvas)

        self.canvas.after(100, self.deplacer_image)

    def missiles(self, coords):
        """Gère les tirs des ennemis"""
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                if randint(1, 50) == 1:  # 2% de chance de tirer par frame
                    tir_ennemi = Tir_Ennemi(self.canvas, ennemi, 0)
                    self.ennemis_tirs.append(tir_ennemi)