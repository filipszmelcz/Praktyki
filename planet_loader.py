import csv
from planet import Planeta

def load_planets(csv_file = "solar_system.csv"):
    planets_data = []

    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return {
            row["planet"]: 
            Planeta(row["planet"], 
                row["mass"], 
                row["radius"], 
                row["gravitation"], 
                row["distance"]) 
                for row in reader
                }
    except FileNotFoundError:
        print(f"Plik {csv_file} nie znaleziony!")


# planets = load_planets()
# for key, value in planets.items():
#     print(value.info())
#                 # planets_data.append({
                #     "planet": row["planet"],
                #     "mass": row["mass"],
                #     "radius": float(row["radius"]),
                #     "gravitation": float(row["gravitation"]),
                #     "distance": int(row["distance"])