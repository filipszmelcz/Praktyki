import csv
from planet import Planeta

def load_planets(csv_file = "solar_system.csv"):
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
