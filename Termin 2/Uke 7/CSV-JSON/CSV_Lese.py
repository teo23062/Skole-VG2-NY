import pandas as pd
import csv
import json

# Henter filplasering til JSON filen som informasjonen skal bli satt inn
json_path = r"C:\Users\teo23062\OneDrive - Vestfold og Telemark fylkeskommune\Skole VG2\Utvikling VG2\Uke 7\CSV-JSON\ny.json"

# Henter CSV filen med data
csv_path = r"C:\Users\teo23062\OneDrive - Vestfold og Telemark fylkeskommune\Skole VG2\Utvikling VG2\Uke 7\CSV-JSON\ansatte.csv"
df = pd.read_csv(csv_path)

# Lager en funskjon som skjører når den har en path for hver av de
def CSV_til_JSON(csv_path, json_path):
    data_dict = {} # Lager en dictionary som lagrer data

    with open(csv_path, encoding = 'utf-8') as csv_fil_hondterer:
        csv_leser = csv.DictReader(csv_fil_hondterer)

        for rows in csv_leser:
            key = rows['a-nr']
            data_dict[key] = rows

    with open(json_path, 'w', encoding = 'utf-8') as json_fil_hondterer:
        json_fil_hondterer.write(json.dumps(data_dict, indent = 4))
 
CSV_til_JSON(csv_path, json_path)