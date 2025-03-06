from space_travel_calculator import *
from planet import Planeta
from planet_loader import *
from search_engine_for_planet_info import planets
from transport_loader import *

transport = load_transport()
solar_system = load_planets()

def menu():
    while True:
        choice = int(input("0 - planet info, 1 - space travel calculator, 2 - planets info, 3 - end: "))
        if choice == 0:
            planets(solar_system)
        if choice == 1:
            calculator(solar_system, transport)
        if choice == 2:
            for key, value in solar_system.items():
                print(value.info())
        if choice == 3:
            break
        if choice not in [0,1,2,3]:
            print("Zły wybór")
            continue
if __name__ == "__main__":
    menu()