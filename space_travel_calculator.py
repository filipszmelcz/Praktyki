from planet_loader import load_planets
solar_system = load_planets()

transport = {
    "Speed ​​of light" : 1079252849,
    "Voyager 1" : 61200,
    "Falcon 9" : 39600,
}

def calculator():
    start = input("Podaj planetę startową: ")
    if start not in solar_system:
        while True:
            print("Zła planet!!!!")
            start = input("Podaj planetę startową: ")
            if start in solar_system:
                break
    dest = input("Podaj planetę docelową: ")
    if dest not in solar_system:
        while True:
            print("Zła planet!!!!")
            dest = input("Podaj planetę docelową: ")
            if dest in solar_system:
                break
    trans = input("Podaj sposób transportu (Speed ​​of light, Voyager 1, Falcon 9): ")
    if trans not in transport:
        while True:
            print("Nie ma takiej opcji!!!!")
            trans = input("Podaj sposób transportu (Speed ​​of light, Voyager 1, Falcon 9): ")
            if trans in transport:
                break
    v = transport.get(trans)
    s = abs(int(solar_system.get(dest).distance) - int(solar_system.get(start).distance))
    t = int(s/v)
    print(f"Czas podróży: {t} dni")
calculator()

