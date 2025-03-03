Solar_System = {
    "Merkury": {"Masa:" : "3,3011 x 10²³ kg", "Promień: " : "2 439,7 km", "Grawitacja: " : "3,7 m/s²", "Odległośc od Słońca: " : "57,9 mln km"},
    "Wenus": {"Masa:" : "4,8675 x 10²⁴ kg", "Promień: " : "6 051,8 km", "Grawitacja: " : "8,87 m/s²", "Odległość od Słońca: " : "108,2 mln km"},
    "Ziemia": {"Masa:" : "5,97237 x 10²⁴ kg", "Promień: " : "6 371 km", "Grawitacja: " : "9,81 m/s²", "Odległość od Słońca: " : "149,6 mln km"},
    "Mars": {"Masa:" : "6,4171 x 10²³ kg", "Promień: " : "3 389,5 km", "Grawitacja: " : "3,71 m/s²", "Odległośc od Słońca: " : "227,9 mln km"},
    "Jowisz": {"Masa:" : "1,8982 x 10²⁷ kg", "Promień: " : "69 911 km", "Grawitacja: " : "24,79 m/s²", "Odległośc od Słońca: " : "778,3 mln km"},
    "Saturn": {"Masa:" : "5,6834 x 10²⁶ kg", "Promień: " : "58 232 km", "Grawitacja: " : "10,44 m/s²", "Odległośc od Słońca: " : "1 427,0 mln km"},
    "Uran": {"Masa:" : "8,6810 x 10²⁵ kg", "Promień: " : "25 362 km", "Grawitacja: " : "8,69 m/s²", "Odległośc od Słońca: " : "2 871,0 mln km"},
    "Neptun": {"Masa:" : "1,02413 x 10²⁶ kg", "Promień: " : "24 622 km", "Grawitacja: " : "11,15 m/s²", "Odległośc od Słońca: " : "4 498,3 mln km"}
}

def Planets():
    planet = input("Wybierz planetę: ")
    if planet in Solar_System:
        for key, value in Solar_System[planet].items():
            print(key, value)

Planets()