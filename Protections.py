class Protections:
    def __init__(self, canvas, width, y_position, cube_size=20, block_width=3, block_height=3, block_gap=50):
        """
        Initialise les protections.
        - `cube_size`: Taille d'un cube (largeur/hauteur en pixels).
        - `block_width`: Nombre de blocs horizontaux.
        - `block_height`: Nombre de lignes de cubes par bloc.
        - `block_gap`: Espace entre chaque bloc.
        """
        self.canvas = canvas
        self.width = width
        self.y_position = y_position  # Position verticale initiale
        self.cube_size = cube_size  # Taille des cubes
        self.block_width = block_width  # Nombre de blocs horizontaux
        self.block_height = block_height  # Nombre de lignes de cubes dans un bloc
        self.block_gap = block_gap  # Espace entre chaque bloc
        self.protections = []  # Stocker les rectangles créés
        self.create_protections()

    def create_protections(self):
        # Calcul de la largeur d'un bloc (cubes)
        block_total_width = self.block_width * self.cube_size  # Pas d'espace entre cubes

        # Calcul du nombre de blocs qui tiennent sur la largeur
        num_blocks = self.width // block_total_width

        for block_index in range(num_blocks):  # Pour chaque bloc
            block_x_start = block_index * (block_total_width + self.block_gap)  # Début horizontal de chaque bloc
            for row in range(self.block_height):  # Pour chaque ligne de cubes dans un bloc
                for col in range(self.block_width):  # Pour chaque cube dans une ligne
                    x1 = block_x_start + col * self.cube_size
                    y1 = self.y_position + row * self.cube_size
                    x2 = x1 + self.cube_size
                    y2 = y1 + self.cube_size
                    cube = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="gray", outline="black"
                    )
                    self.protections.append(cube)