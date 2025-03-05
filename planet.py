class Planeta:
    def __init__(self, nazwa, masa, promien, grawitacja, odleglosc_od_slonca):
        self.nazwa = nazwa
        self.masa = masa
        self.promien = promien
        self.grawitacja = grawitacja
        self.odleglosc_od_slonca = odleglosc_od_slonca
    def info(self):
        return(f"Planeta: {self.nazwa}\n"
               f"Masa:{self.masa} kg\n"
               f"Promien: {self.promien} km\n"
               f"Grawitacja: {self.grawitacja} m/s²\n"
               f"Odleglosc od slonca: {self.odleglosc_od_slonca} mln km\n")
        

