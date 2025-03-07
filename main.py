from space_travel_calculator import calculator
from planet_loader import load_planets
from search_engine_for_planet_info import planets
from transport_loader import load_transport

transport = load_transport()
solar_system = load_planets()

option = {
    "0": lambda: planets(solar_system),
    "1": lambda: calculator(solar_system, transport),
    "2": lambda: [print(value.info()) for key, value in solar_system.items()],
}


def menu():
    while True:
        choice = input("0 - planet info, 1 - space travel calculator, 2 - planets info, 3 - end: ")
        if choice in option:
            option.get(choice)()
        if choice == "3":
            break
        elif choice not in ["0","1","2","3"]:
            print("Zły wybór")
            continue
if __name__ == "__main__":
    menu()