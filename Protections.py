class Protections:
    def __init__(self, canvas, width, y_position, cube_size=10):
        self.canvas = canvas
        self.width = width
        self.y_position = y_position
        self.cube_size = cube_size
        self.protections = []  # Stocker les rectangles créés
        self.create_protections()

    def create_protections(self):
        for x in range(0, self.width, self.cube_size):
            cube = self.canvas.create_rectangle(
                x, self.y_position,
                x + self.cube_size, self.y_position + self.cube_size,
                fill="gray", outline=""
            )
            self.protections.append(cube)