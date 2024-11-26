# coding: utf-8

import tkinter as tk
from Tir_Ennemi import Tir_Ennemi 
from random import randint 

class Ennemi:# on défini les énnemis
    def __init__(self, canvas):
        self.canvas = canvas
        self.dx = -3
        self.image = tk.PhotoImage(file="ressources/ennemi.png")
        self.image = self.image.subsample(9, 12)  
        self.compteur = 0
        for n in range (5) :
            self.rect = self.canvas.create_rectangle(60 + n*75 - 10, 50 - 10, 60 + n*75 + 10, 50 + 10, outline="blue", width=2, tags="groupe")
            self.deplacer_image()

    def deplacer_image(self): # on fait se déplacer le groupe d'ennemis
        self.canvas.move("groupe", self.dx, 0)
        coords = []
        for nom in self.canvas.find_withtag("groupe"):
            coords.append(self.canvas.coords(nom))
        maxX = 0 
        for val in coords :
            if val[0] >= maxX :
                maxX= val[0]
        minX = 600
        for val in coords :
            if val[0] <= minX :
                minX= val[0]
        if minX <= 35 or maxX >= 635:
            self.dx *= (-1)  
        self.missiles(coords )
        self.canvas.after(100, self.deplacer_image)

    def missiles (self , coords,): #et on les fait tirer 
        if self.compteur == 15 : # on tire une fois tt les 5 tours  #on remet de l'aleatoire pour ralentir la cadence de tir 
            radm = randint (0,len(coords)-1)
            start =  (coords[radm-1][0])
            Tir_Ennemi(self.canvas , start, coords[radm-1][1])
            self.compteur = 0 
        else :
            self.compteur +=1

