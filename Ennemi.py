# coding: utf-8
import tkinter as tk
from Tir_Ennemi import Tir_Ennemi
from random import randint
from PIL import Image, ImageTk
from Boss import Ennemi_bonus 

class Ennemi:
    def __init__(self, canvas):
        self.canvas = canvas
        self.dx = -3
        self.image = Image.open("ressources/ennemiblanc.png")
        self.image = self.image.resize((40, 40))
        self.photo = ImageTk.PhotoImage(self.image)
        self.compteur = 0
        self.descente_compteur = 0
        self.apparition_bonus = 0
        self.ennemis = []
        self.ennemis_tirs = []
        self.limite_y = 400  # Hauteur des protections grises
        
        # Créer les ennemis (première rangée)
        for n in range(8):
            ennemi = self.canvas.create_image(60 + n*75, 50, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        
        # Créer les ennemis (deuxième rangée)
        for n in range(8):
            ennemi = self.canvas.create_image(60 + n*75, 100, image=self.photo, tags="groupe")
            self.ennemis.append(ennemi)
        
        # Démarrer le mouvement
        self.deplacer_image()

    def deplacer_image(self):
        if not self.ennemis:
            return
        
        # Déplacer le groupe d'ennemis
        self.canvas.move("groupe", self.dx, 0)
        
        # Vérifier la position y maximale des ennemis
        max_y = 0
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                y = self.canvas.coords(ennemi)[1]
                if y > max_y:
                    max_y = y
        
        # Si les ennemis sont trop bas, game over
        if max_y >= self.limite_y:
            fenetre = self.canvas.winfo_toplevel()
            fenetre.game_over()
            return
        
        # Collecter les coordonnées actuelles des ennemis existants
        coords = []
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                coords.append(self.canvas.coords(ennemi)[0])
        
        if not coords:
            return
        
        minX = min(coords)
        maxX = max(coords)
        
        if minX <= 35 or maxX >= 635:
            self.dx *= -1
        
        # Générer des missiles
        self.missiles(coords)
        
        # Vérifier les collisions des tirs ennemis
        for tir_ennemi in list(self.ennemis_tirs):
            try:
                tir_ennemi.CollisionJoueur()
            except Exception:
                self.ennemis_tirs.remove(tir_ennemi)
        
        # Incrémenter les compteurs
        self.descente_compteur += 1
        self.apparition_bonus += 1
        
        # Descendre tous les 30 * 100ms = 3000ms
        if self.descente_compteur >= 30:
            self.canvas.move("groupe", 0, 20)
            self.descente_compteur = 0
        
        # Créer le boss bonus
        if self.apparition_bonus == 160:
            self.apparition_bonus = 0
            self.boss = Ennemi_bonus(self.canvas)

        # Continuer le mouvement
        self.canvas.after(100, self.deplacer_image)

    def missiles(self, coords):
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                if randint(1, 50) == 1:
                    tir_ennemi = Tir_Ennemi(self.canvas, ennemi, 0)
                    self.ennemis_tirs.append(tir_ennemi)