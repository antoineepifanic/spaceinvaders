class Tir_Ennemi:
    def __init__(self, canvas, start, altitude):
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(start-4, altitude, start+4, altitude + 15, fill="blue")
        self.dy = 5
        self.can_coll = True
        self.avancer()

    def avancer(self):
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        # Vérifier la collision avec le vaisseau
        if self.CollisionJoueur():
            self.canvas.delete(self.rect)
            self.can_coll = False
            return

        self.canvas.after(20, self.avancer)

    def CollisionJoueur(self):
        vaisseau = self.canvas.find_withtag("vaisseau")
        if vaisseau and self.can_coll:
            coords_vaisseau = self.canvas.bbox(vaisseau)
            coords_tir_ennemi = self.canvas.bbox(self.rect)
            if (coords_tir_ennemi[2] > coords_vaisseau[0] and
                coords_tir_ennemi[0] < coords_vaisseau[2] and
                coords_tir_ennemi[3] > coords_vaisseau[1] and
                coords_tir_ennemi[1] < coords_vaisseau[3]):
                print("Collision avec le vaisseau !")
                # Ajouter le code pour gérer la collision avec le vaisseau (perdre des vies, etc.)
                return True
        return False