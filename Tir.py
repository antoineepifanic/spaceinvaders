# coding: utf-8

class Tir:
    def __init__(self, canvas, start):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(start-5, 470, start+5, 490, fill="red")
        self.dy = -5
        self.points_par_ennemi = 25
        self.avancer()

    def avancer(self):
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        
        # Vérifier d'abord la collision avec les protections
        if self.collision_protection():
            self.canvas.delete(self.rect)
            return
            
        # Ensuite vérifier la collision avec les ennemis
        if self.collision_ennemi():
            return
            
        # Si le tir sort de l'écran
        if coords[3] <= 0:
            self.canvas.delete(self.rect)
            return
            
        self.canvas.after(20, self.avancer)

    def collision_protection(self):
        coords_tir = self.canvas.bbox(self.rect)
        # Trouver tous les rectangles gris (protections)
        all_items = self.canvas.find_all()
        for item in all_items:
            # Vérifier si l'item est un rectangle gris
            if self.canvas.type(item) == "rectangle":
                fill_color = self.canvas.itemcget(item, "fill")
                if fill_color == "gray":
                    coords_protection = self.canvas.bbox(item)
                    if coords_protection:  # Vérifier si le rectangle existe toujours
                        if (coords_tir[2] > coords_protection[0] and
                            coords_tir[0] < coords_protection[2] and
                            coords_tir[3] > coords_protection[1] and
                            coords_tir[1] < coords_protection[3]):
                            # Collision détectée, supprimer le bloc de protection
                            self.canvas.delete(item)
                            return True
        return False

    def collision_ennemi(self):
        coords_tir = self.canvas.bbox(self.rect)
        ennemis = self.canvas.find_withtag("groupe")
        for ennemi in ennemis:
            coords_ennemi = self.canvas.bbox(ennemi)
            if coords_ennemi and (coords_tir[2] > coords_ennemi[0] and
                coords_tir[0] < coords_ennemi[2] and
                coords_tir[3] > coords_ennemi[1] and
                coords_tir[1] < coords_ennemi[3]):
                self.canvas.delete(self.rect)
                self.canvas.delete(ennemi)
                # Mettre à jour le score
                fenetre = self.canvas.winfo_toplevel()
                fenetre.score += self.points_par_ennemi
                fenetre.update_score()
                self.canvas.update()
                return True
        return False