# coding: utf-8
import tkinter as tk
from Tir_Ennemi import Tir_Ennemi
from random import randint
from PIL import Image, ImageTk 

class Ennemi_bonus :
    def bonus (self, canvas, altitude):
        self.canvas = canvas
        self.dx = 7
        self.image = Image.open("ressources/bonus.png")
        self.image = self.image.resize((40, 40))
        self.photo = ImageTk.PhotoImage(self.image)
        bonus=self.canvas.create_image(0 , 300, image=self.photo, tags="bonus")

        self.deplacer()
    
    def deplacer (self):
        if not self.ennemis:
            return
        self.canvas.move("bonus", self.dx, 0)
        coords = []
        coords.append(self.canvas.coords(self.bonus)[0])
        if not coords:
            return
        self.fin_de_partie()
        if max(coords) >= 750 :
            self.canvas.delet(self.bonus)
        self.canvas.after(100, self.deplacer_image)