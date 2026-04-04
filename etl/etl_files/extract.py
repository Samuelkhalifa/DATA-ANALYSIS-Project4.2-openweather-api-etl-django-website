import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract(cities):

    api_key = os.getenv("API_KEY")

    raw_data = []

    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            raw_data.append(data)
            print(f"appended data for {city}")
        else:
            print("Error :", response.status_code)
            print(f"No matching with city {city}")

    return raw_data