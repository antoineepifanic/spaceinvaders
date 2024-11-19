# coding: utf-8

class Tir:
    def __init__(self, canvas, start):
        self.canvas = canvas
        
        self.view = self.canvas.create_rectangle(start-5, 370, start+5, 390, fill="red")

    def avancer(self):
        self.view.move(0, -10)
