class Planeta:
    def __init__(self, nazwa, mass, radius, gravitation, distance):
        self.nazwa = nazwa
        self.mass = mass
        self.radius = radius
        self.gravitation = gravitation
        self.distance = distance
        
    def info(self):
        return(f"Planeta: {self.nazwa}\n"
               f"Masa:{self.mass} kg\n"
               f"Promien: {self.radius} km\n"
               f"Grawitacja: {self.gravitation} m/s²\n"
               f"Odleglosc od slonca: {self.distance} mln km\n")
    