def transform(raw_data):

    transformed_data = []

    for i in raw_data:
        i_transformed = {
            "city": i.get("name"),
            "country": i.get("sys", {}).get("country"),
            "latitude": i.get("coord", {}).get("lat"),
            "longitude": i.get("coord", {}).get("lon"),
            "weather": i.get("weather")[0].get("main"),
            "weather_description": i.get("weather")[0].get("description"),
            "weather_icon": f"https://openweathermap.org/img/wn/{i.get("weather")[0].get("icon")}@2x.png",
            "temperature": i.get("main", {}).get("temp"),
            "temperature_feels_like": i.get("main", {}).get("feels_like"),
            "temperature_min": i.get("main", {}).get("temp_min"),
            "temperature_max": i.get("main", {}).get("temp_max"),
        }
        transformed_data.append(i_transformed)

    return transformed_data
        