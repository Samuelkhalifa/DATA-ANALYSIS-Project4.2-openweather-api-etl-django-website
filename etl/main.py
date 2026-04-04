from etl.etl_files.extract import extract
from etl.etl_files.transform import transform
from etl.etl_files.load import load
import csv
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "csv_data", "world_cities_sample.csv"))
cities = df["name_en"].to_list()

def main(cities):    

    # Main intructions of the program

    raw_data = extract(cities)
    transformed_data = transform(raw_data)
    with open(os.path.join(BASE_DIR, "csv_data", "weather_data.csv"), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=transformed_data[0].keys())
        writer.writeheader()
        writer.writerows(transformed_data)
    #load(transformed_data)

main(cities)