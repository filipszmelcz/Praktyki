def calculator(solar_system, transport):
    while True:
        start = input("Podaj planetę startową: ")
        if start in solar_system:
            break
        print("Zła planet!!!!")
    while True:
        dest = input("Podaj planetę docelową: ")
        if dest in solar_system:
            break            
        print("Zła planet!!!!")
    while True:
        trans = input("Podaj sposób transportu (Speed_of_light, Voyager 1, Falcon 9): ")
        if trans in transport:
            break
        print("Nie ma takiej opcji!!!!")
    
    v = transport.get(trans)
    s = abs(int(solar_system.get(dest).distance) - int(solar_system.get(start).distance))
    t = int(s/v)
    print(f"Czas podróży: {t} dni")



