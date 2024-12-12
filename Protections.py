class Protections:
    def __init__(self, canvas, width, y_position, cube_size=20):
        self.canvas = canvas
        self.width = width
        self.y_position = y_position 
        self.cube_size = cube_size  # Taille des cubes
        self.protections = []  # Stocker les rectangles créés
        self.create_protections()

    def create_protections(self):
        for row in range(3):  # Pour deux lignes
            for x in range(0, self.width, self.cube_size):
                cube = self.canvas.create_rectangle(
                    x, 
                    self.y_position + row * self.cube_size,  # Décaler chaque ligne verticalement
                    x + self.cube_size, 
                    self.y_position + (row + 1) * self.cube_size,
                    fill="gray", 
                    outline="black"  # Bordure noire
                )
                self.protections.append(cube)