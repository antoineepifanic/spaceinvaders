# coding: utf-8
"""
Tir.py
Gestion des tirs du joueur dans le jeu Space Invaders

Ce module gère le comportement des missiles tirés par le vaisseau du joueur,
incluant leur déplacement et leurs interactions avec les éléments du jeu.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

class Tir:
    def __init__(self, canvas, start):
        """
        Initialise un tir du joueur.

        Args:
            canvas (tk.Canvas): Zone de dessin du jeu
            start (int): Position horizontale de départ du tir
        """
        self.canvas = canvas
        self.rect = self.canvas.create_rectangle(
            start-5, 470, start+5, 490, fill="red"
        )
        self.dy = -5
        self.points_par_ennemi = 25
        self.points_boss = 150
        self.avancer()

    def avancer(self):
        """
        Déplace le missile vers le haut et gère ses interactions.
        
        Vérifie les collisions avec les protections, le boss et les ennemis.
        Supprime le missile s'il sort de l'écran.
        """
        self.canvas.move(self.rect, 0, self.dy)
        coords = self.canvas.coords(self.rect)
        
        # Vérifier la collision avec les protections
        if self.collision_protection():
            self.canvas.delete(self.rect)
            return
            
        # Vérifier la collision avec le boss
        if self.collision_boss():
            return
            
        # Vérifier la collision avec les ennemis
        if self.collision_ennemi():
            return
            
        # Supprimer le tir s'il sort de l'écran
        if coords[3] <= 0:
            self.canvas.delete(self.rect)
            return
            
        self.canvas.after(20, self.avancer)

    def collision_protection(self):
        """
        Détecte et gère les collisions avec les blocs de protection.

        Returns:
            bool: True si une collision est détectée, False sinon
        """
        coords_tir = self.canvas.bbox(self.rect)
        all_items = self.canvas.find_all()
        for item in all_items:
            if (self.canvas.type(item) == "rectangle" and 
                self.canvas.itemcget(item, "fill") == "gray"):
                coords_protection = self.canvas.bbox(item)
                if coords_protection and self._verifier_collision(coords_tir, coords_protection):
                    self.canvas.delete(item)
                    return True
        return False

    def collision_boss(self):
        """
        Détecte et gère les collisions avec l'ennemi bonus.

        Returns:
            bool: True si une collision est détectée, False sinon
        """
        coords_tir = self.canvas.bbox(self.rect)
        boss = self.canvas.find_withtag("boss")
        
        for boss_item in boss:
            coords_boss = self.canvas.bbox(boss_item)
            if coords_boss and self._verifier_collision(coords_tir, coords_boss):
                self.canvas.delete(self.rect)
                self.canvas.delete(boss_item)
                fenetre = self.canvas.winfo_toplevel()
                fenetre.score += self.points_boss
                fenetre.update_score()
                return True
        return False

    def collision_ennemi(self):
        """
        Détecte et gère les collisions avec les ennemis standards.

        Returns:
            bool: True si une collision est détectée, False sinon
        """
        coords_tir = self.canvas.bbox(self.rect)
        ennemis = self.canvas.find_withtag("groupe")
        for ennemi in ennemis:
            coords_ennemi = self.canvas.bbox(ennemi)
            if coords_ennemi and self._verifier_collision(coords_tir, coords_ennemi):
                self.canvas.delete(self.rect)
                self.canvas.delete(ennemi)
                
                # Mettre à jour le score
                fenetre = self.canvas.winfo_toplevel()
                fenetre.score += self.points_par_ennemi
                fenetre.update_score()

                # Vérifier s'il reste des ennemis
                ennemis_restants = list(self.canvas.find_withtag("groupe"))
                if len(ennemis_restants) == 0:
                    self.canvas.after(10, lambda: fenetre.game_over())
                
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