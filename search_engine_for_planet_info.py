solar_system = {
    "Mercury": {"Masa:" : "3,3011 x 10²³ kg", "Promień: " : "2 439,7 km", "Grawitacja: " : "3,7 m/s²", "Odległośc od Słońca(km): " : 57900000},
    "Venus": {"Masa:" : "4,8675 x 10²⁴ kg", "Promień: " : "6 051,8 km", "Grawitacja: " : "8,87 m/s²", "Odległośc od Słońca(km): " : 108200000},
    "Earth": {"Masa:" : "5,97237 x 10²⁴ kg", "Promień: " : "6 371 km", "Grawitacja: " : "9,81 m/s²", "Odległośc od Słońca(km): " : 149600000},
    "Mars": {"Masa:" : "6,4171 x 10²³ kg", "Promień: " : "3 389,5 km", "Grawitacja: " : "3,71 m/s²", "Odległośc od Słońca(km): " : 227900000},
    "Jupiter": {"Masa:" : "1,8982 x 10²⁷ kg", "Promień: " : "69 911 km", "Grawitacja: " : "24,79 m/s²", "Odległośc od Słońca(km): " : 778300000},
    "Saturn": {"Masa:" : "5,6834 x 10²⁶ kg", "Promień: " : "58 232 km", "Grawitacja: " : "10,44 m/s²", "Odległośc od Słońca(km): " : 1427000000},
    "Uranus": {"Masa:" : "8,6810 x 10²⁵ kg", "Promień: " : "25 362 km", "Grawitacja: " : "8,69 m/s²", "Odległośc od Słońca(km): " : 2871000000},
    "Neptune": {"Masa:" : "1,02413 x 10²⁶ kg", "Promień: " : "24 622 km", "Grawitacja: " : "11,15 m/s²", "Odległośc od Słońca(km): " : 4498300000}
}

def planets():
    while True:
        planet = input("Wybierz planetę lub 0, żeby zakończyć program: ")
        if planet == "0":
            break
        if not planet:
            print("Proszę podać nazwę planety.")
            continue
        if planet in solar_system:
            for key, value in solar_system[planet].items():
                print(key, value)
        else:
            print("Nie ma takiej planety w układzie słonecznym")

