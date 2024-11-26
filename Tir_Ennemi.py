# coding: utf-8

class Tir_Ennemi:
    def __init__(self, canvas, start, altitude):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(start-4, altitude, start+4, altitude + 15, fill="blue")
        self.dy = 5
        self.avancer() 
    def avancer(self) :
        self.canvas.move(self.rect,0, self.dy)
        coords = self.canvas.coords(self.rect)
        if coords[3] >= 650:
            self.canvas.delete(self.rect)
            return
        self.canvas.after(20, self.avancer)

