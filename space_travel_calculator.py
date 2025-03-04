from search_engine_for_planet_info import solar_system

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

