# coding: utf-8


class Tir:
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
        
        # Ajoute des marges pour rendre la collision plus permissive
        marge = 5  # Ajuste cette marge si nécessaire

        for ennemi in ennemis:
            coords_ennemi = self.canvas.coords(ennemi)

            # Vérifie si les coordonnées de l'ennemi sont valides
            if not coords_ennemi or len(coords_ennemi) < 4:
                continue

            # Vérification de collision avec marge
            if (coords_tir[2] > coords_ennemi[0] - marge and  # Bord droit du tir dépasse le bord gauche de l'ennemi
                coords_tir[0] < coords_ennemi[2] + marge and  # Bord gauche du tir avant le bord droit de l'ennemi
                coords_tir[3] > coords_ennemi[1] - marge and  # Bas du tir dépasse le haut de l'ennemi
                coords_tir[1] < coords_ennemi[3] + marge):    # Haut du tir avant le bas de l'ennemi
                
                # Collision détectée : supprimer le tir et l'ennemi
                self.canvas.delete(self.rect)
                self.canvas.delete(ennemi)

                return True  # Collision détectée
        
        return False  # Aucune collision détectée