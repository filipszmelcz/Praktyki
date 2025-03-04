from search_engine_for_planet_info import solar_system
# solar_system = {
#     "Merkury": 57900000,
#     "Wenus": 108200000,
#     "Ziemia": 149600000,
#     "Mars": 227900000,
#     "Jowisz": 778300000, 
#     "Saturn":1427000000,
#     "Uran": 2871000000,
#     "Neptun": 4498300000,
# }

transport = {
    "Prędkość światła" : 1079252849,
    "Voyager 1" : 61200,
    "Falcon 9" : 39600,
}

def calculator():
    start = input("Podaj planetę startową: ")
    dest = input("Podaj planetę docelową: ")
    trans = input("Podaj sposób transportu (Prędkość światła, Voyager 1, Falcon 9): ")
    v = transport.get(trans)
    s = abs(int(solar_system.get(dest).get("Odległośc od Słońca(km): ")) - int(solar_system.get(start).get("Odległośc od Słońca(km): ")))
    t = int(s/v)
    print(f"Czas podróży: {t} dni")
calculator()
    # if solar_system[dest] - solar_system[start] > 0:
    #     s = solar_system[dest] - solar_system[start]
    #     v = transport[trans]
    #     t = int(s/v)
    #     print(f"Czas podróży: {t} dni")
    # else:
    #     s = solar_system[start] - solar_system[dest]
    #     v = transport[trans]
    #     t = int(s/v)
    # print(f"Czas podróży: {t} dni")
