import csv

def load_transport(csv_file = "transport.csv"):
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return{
                row["object"]: float(row["velocity"])
                for row in reader
            }
    except FileNotFoundError:
        print(f"Plik {csv_file} nie znaleziony!")

