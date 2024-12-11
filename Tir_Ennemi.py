class Tir_Ennemi:
    def __init__(self, canvas, start, altitude):
        self.canvas = canvas
        # Utiliser les coordonnées actuelles de l'ennemi pour le tir
        current_coords = self.canvas.coords((start,))
        self.rect = self.canvas.create_rectangle(
            current_coords[0]-4, 
            current_coords[1] + 15,  # Partir du bas de l'ennemi
            current_coords[0]+4, 
            current_coords[1] + 30,  # Un peu plus bas
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
        
        # Vérifier la collision avec le vaisseau
        if self.CollisionJoueur():
            self.canvas.delete(self.rect)
            self.can_coll = False
            return
        
        self.canvas.after(20, self.avancer)

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
                # Récupérer l'instance du joueur à partir de la fenêtre
                joueur = self.canvas.winfo_toplevel().joueur
                game_over = joueur.perdre_vie()
                if game_over:
                    print("Game Over !")
                return True
        return False