# coding: utf-8

class Tir:
    def __init__(self, canvas, start):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(start-5, 370, start+5, 390, fill="red")
        self.dy = -5
        self.avancer() 
    def avancer(self) :
        self.canvas.move(self.rect,0, self.dy)
        coords = self.canvas.coords(self.rect)
        if coords[3] <= 0:
            self.canvas.delete(self.rect)
            return
        self.canvas.after(20, self.avancer)

