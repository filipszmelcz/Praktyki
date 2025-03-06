def planets(solar_system):
    while True:
        planet = input("Wybierz planetę lub 0, żeby zakończyć program: ")
        if planet == "0":
            break
        if not planet:
            print("Proszę podać nazwę planety.")
            continue
        if planet in solar_system:
                print(solar_system.get(planet).info())
        else:
            print("Nie ma takiej planety w układzie słonecznym!!!!")

