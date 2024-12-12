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
        self.appa_bonu =0  # Nouveau compteur pour la descente
        self.ennemis = []
        self.ennemis_tirs = []
        
        
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
        # Vérifier si des ennemis existent encore
        if not self.ennemis:
            return
        
        # Déplacer le groupe d'ennemis
        self.canvas.move("groupe", self.dx, 0)
        
        # Collecter les coordonnées actuelles des ennemis existants
        coords = []
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_withtag("groupe"):
                coords.append(self.canvas.coords(ennemi)[0])
        
        # S'il n'y a plus de coordonnées, arrêter
        if not coords:
            return
        
        # Trouver les positions extrêmes
        minX = min(coords)
        maxX = max(coords)
        
        # Inverser la direction si nécessaire
        if minX <= 35 or maxX >= 635:
            self.dx *= -1
        
        # Vérifier la fin de partie
        self.fin_de_partie()
        
        # Générer des missiles
        self.missiles(coords)
        
        # Vérifier les collisions des tirs ennemis
        for tir_ennemi in list(self.ennemis_tirs):  # Utiliser une copie de liste
            try:
                tir_ennemi.CollisionJoueur()
            except Exception:
                # Supprimer le tir s'il y a une erreur
                self.ennemis_tirs.remove(tir_ennemi)
        
        # Incrémenter le compteur de descente
        self.descente_compteur += 1
        self.appa_bonu +=1
        
        # Descendre tous les 50 * 100ms = 5000ms (5 secondes)
        if self.descente_compteur >= 30:
            self.canvas.move("groupe", 0, 20)  # Descendre de 100 pixels
            self.descente_compteur = 0
        
        if self.appa_bonu == 160 :
            bonus = Ennemi_bonus
        # Continuer le mouvement
        self.canvas.after(100, self.deplacer_image)

    def missiles(self, coords):
        # Parcourir tous les ennemis
        for ennemi in self.ennemis:
            if ennemi in self.canvas.find_all():
                # Générer un nombre aléatoire pour décider de tirer
                # Vous pouvez ajuster la probabilité en changeant le nombre
                if randint(1, 50) == 1:  # 1% de chance de tirer à chaque frame
                    tir_ennemi = Tir_Ennemi(self.canvas, ennemi, 0)
                    self.ennemis_tirs.append(tir_ennemi)

    def fin_de_partie(self):
        if len(self.ennemis) == 0:
            print("Vous avez gagné")
            # Ajouter ici votre logique de fin de partie