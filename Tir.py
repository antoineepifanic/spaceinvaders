# coding: utf-8


class Tir:# la classe tire on cré un rectangle sur la position du joueur et on le fait avancer vers le haut.
    def __init__(self, canvas, start):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(start-5, 370, start+5, 390, fill="red")
        self.dy = -5
        self.avancer() 
    
    def avancer(self):
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        if self.collision():
            return
        if coords[3] <= 0:
            self.canvas.delete(self.rect)
            return
        self.canvas.after(20, self.avancer)
    
    def collision(self):
        coords_tir = self.canvas.coords(self.rect)
        ennemis = self.canvas.find_withtag("groupe")
        for ennemi in ennemis:
            coords_ennemi = self.canvas.coords(ennemi)
            if (coords_tir[2] > coords_ennemi[0] and  
                coords_tir[0] < coords_ennemi[2] and  
                coords_tir[3] > coords_ennemi[1] and  
                coords_tir[1] < coords_ennemi[3]): 
                self.canvas.delete(self.rect)        
                self.canvas.delete(ennemi)
                return True  
        return False  
