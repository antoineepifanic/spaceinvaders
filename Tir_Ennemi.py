class Tir_Ennemi:
    def __init__(self, canvas, start, altitude):
        self.canvas = canvas
        current_coords = self.canvas.coords((start,))
        self.rect = self.canvas.create_rectangle(
            current_coords[0]-4, 
            current_coords[1] + 15,
            current_coords[0]+4, 
            current_coords[1] + 30,
            fill="blue"
        )
        self.dy = 5
        self.can_coll = True
        self.avancer()

    def avancer(self):
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        
        # Supprimer le tir s'il sort de l'écran
        if coords[3] >= self.canvas.winfo_height():
            self.canvas.delete(self.rect)
            return
        
        # Vérifier d'abord la collision avec les protections
        if self.CollisionProtection():
            self.canvas.delete(self.rect)
            return
        
        # Ensuite vérifier la collision avec le vaisseau
        if self.CollisionJoueur():
            self.canvas.delete(self.rect)
            self.can_coll = False
            return
        
        self.canvas.after(20, self.avancer)

    def CollisionProtection(self):
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

    def CollisionJoueur(self):
        vaisseau = self.canvas.find_withtag("vaisseau")
        if vaisseau:
            coords_vaisseau = self.canvas.bbox(vaisseau)
            coords_tir_ennemi = self.canvas.bbox(self.rect)
            if (coords_tir_ennemi[2] > coords_vaisseau[0] and
                coords_tir_ennemi[0] < coords_vaisseau[2] and
                coords_tir_ennemi[3] > coords_vaisseau[1] and
                coords_tir_ennemi[1] < coords_vaisseau[3]):
                print("Collision avec le vaisseau !")
                joueur = self.canvas.winfo_toplevel().joueur
                game_over = joueur.perdre_vie()
                if game_over:
                    print("Game Over !")
                return True
        return False