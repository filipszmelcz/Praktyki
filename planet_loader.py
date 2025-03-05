import csv
from planet import Planeta

def load_planets(csv_file = "solar_system.csv"):
    planets_data = []

    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                planets_data.append({
                    "planet": row["planet"],
                    "masa": row["masa"],
                    "promien": float(row["promien"]),
                    "grawitacja": float(row["grawitacja"]),
                    "odleglosc_od_slonca": int(row["odleglosc_od_slonca"])
                })
    except FileNotFoundError:
        print(f"Plik {csv_file} nie znaleziony!")
    return planets_data
planets_data = load_planets()

planets = {row["planet"]: Planeta(row["planet"], row["masa"], row["promien"], row["grawitacja"], row["odleglosc_od_slonca"]) for row in planets_data}

for key, value in planets.items():
    print(value.info())