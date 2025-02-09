import math

class Cylinder:

    def __init__(self, radius, height):
            self.radius = radius
            self.height = height

    def  volume(self):
        return math.pi * self.radius ** 2 * self.height

    def bottom_area(self):
        return math.pi * self.radius **2

    def side_area(self):
        return 2 * math.pi * self.radius * self.height

    def total_area(self):
        return 2 * math.pi * self.radius**2 + self.side_area()
    def __repr__(self):
        return (f"Raadius: {self.radius}, \nKõrgus: {self.height}, "
                f"\nRuumala:{self.volume()}, \nPõhjapindala: {self.bottom_area()}, "
                f"\nKüljepindala: {self.side_area()}, "
                f"\nKogu pindala: {self.total_area()}")
