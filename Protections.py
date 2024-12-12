# coding: utf-8
"""
Protections.py
Gestion des protections dans le jeu Space Invaders

Ce module gère la création et le comportement des protections 
qui servent de boucliers pour le joueur contre les tirs ennemis.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

class Protections:
    def __init__(self, canvas, width, y_position, cube_size=20, block_width=3, block_height=3, block_gap=50):
        """
        Initialise les protections défensives du vaisseau.

        Args:
            canvas (tk.Canvas): Zone de dessin pour les protections
            width (int): Largeur totale de la zone de jeu
            y_position (int): Position verticale initiale des protections
            cube_size (int, optional): Taille d'un cube de protection en pixels. Défaut à 20.
            block_width (int, optional): Nombre de cubes horizontaux par bloc. Défaut à 3.
            block_height (int, optional): Nombre de lignes de cubes par bloc. Défaut à 3.
            block_gap (int, optional): Espace entre chaque bloc de protection. Défaut à 50.
        """
        self.canvas = canvas
        self.width = width
        self.y_position = y_position
        self.cube_size = cube_size
        self.block_width = block_width
        self.block_height = block_height
        self.block_gap = block_gap
        self.protections = []  # Liste pour stocker les rectangles de protection
        self.create_protections()

    def create_protections(self):
        """
        Génère les blocs de protection sur le canvas.
        
        Crée une série de blocs de cubes gris qui servent de boucliers 
        pour protéger le vaisseau des tirs ennemis.
        """
        # Calcul de la largeur totale d'un bloc de protection
        block_total_width = self.block_width * self.cube_size

        # Détermination du nombre de blocs pouvant tenir dans la largeur
        num_blocks = self.width // (block_total_width + self.block_gap)

        for block_index in range(num_blocks):
            # Position horizontale du début de chaque bloc
            block_x_start = block_index * (block_total_width + self.block_gap)
            
            # Création des cubes pour chaque bloc
            for row in range(self.block_height):
                for col in range(self.block_width):
                    x1 = block_x_start + col * self.cube_size
                    y1 = self.y_position + row * self.cube_size
                    x2 = x1 + self.cube_size
                    y2 = y1 + self.cube_size
                    
                    # Création du rectangle de protection
                    cube = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="gray", outline="black"
                    )
                    self.protections.append(cube)