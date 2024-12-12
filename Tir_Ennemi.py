# coding: utf-8
"""
Tir_Ennemi.py
Gestion des tirs ennemis dans le jeu Space Invaders

Ce module gère le comportement des missiles tirés par les ennemis,
incluant leur déplacement et leurs interactions avec les éléments du jeu.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

class Tir_Ennemi:
    def __init__(self, canvas, start, altitude):
        """
        Initialise un tir ennemi.

        Args:
            canvas (tk.Canvas): Zone de dessin du jeu
            start (int): Objet ennemi qui tire le missile
            altitude (int, optional): Altitude de départ non utilisée
        """
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
        """
        Déplace le missile vers le bas et gère ses interactions.
        
        Vérifie les collisions avec les protections et le vaisseau.
        Supprime le missile s'il sort de l'écran.
        """
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        
        # Supprimer le tir s'il sort de l'écran
        if coords[3] >= self.canvas.winfo_height():
            self.canvas.delete(self.rect)
            return
        
        # Vérifier la collision avec les protections
        if self.CollisionProtection():
            self.canvas.delete(self.rect)
            return
        
        # Vérifier la collision avec le vaisseau
        if self.CollisionJoueur():
            self.canvas.delete(self.rect)
            self.can_coll = False
            return
        
        self.canvas.after(20, self.avancer)

    def CollisionProtection(self):
        """
        Détecte et gère les collisions avec les blocs de protection.

        Returns:
            bool: True si une collision est détectée, False sinon
        """
        coords_tir = self.canvas.bbox(self.rect)
        all_items = self.canvas.find_all()
        for item in all_items:
            # Vérifier si l'item est un rectangle gris (protection)
            if (self.canvas.type(item) == "rectangle" and 
                self.canvas.itemcget(item, "fill") == "gray"):
                coords_protection = self.canvas.bbox(item)
                if coords_protection and self._verifier_collision(coords_tir, coords_protection):
                    self.canvas.delete(item)
                    return True
        return False

    def CollisionJoueur(self):
        """
        Détecte et gère les collisions avec le vaisseau du joueur.

        Returns:
            bool: True si une collision est détectée, False sinon
        """
        vaisseau = self.canvas.find_withtag("vaisseau")
        if vaisseau:
            coords_vaisseau = self.canvas.bbox(vaisseau)
            coords_tir_ennemi = self.canvas.bbox(self.rect)
            
            if self._verifier_collision(coords_tir_ennemi, coords_vaisseau):
                joueur = self.canvas.winfo_toplevel().joueur
                game_over = joueur.perdre_vie()
                return True
        return False

    def _verifier_collision(self, coords1, coords2):
        """
        Vérifie s'il y a une collision entre deux rectangles.

        Args:
            coords1 (list): Coordonnées du premier rectangle
            coords2 (list): Coordonnées du second rectangle

        Returns:
            bool: True s'il y a collision, False sinon
        """
        return (coords1[2] > coords2[0] and
                coords1[0] < coords2[2] and
                coords1[3] > coords2[1] and
                coords1[1] < coords2[3])