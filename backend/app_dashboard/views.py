from django.shortcuts import render
from etl.etl_files.extract import extract
from etl.etl_files.transform import transform
from etl.main import cities


def home(request):

    data = transform(extract(cities))
    data_array = []

    for d in data:
        data_array.append(d)
    
    selected_city = None
    selected_city_country = None
    selected_city_weather = None
    selected_city_weather_description = None
    selected_city_temperature = None
    selected_city_weather_icon = None

    if request.method == "POST":
        selected_city = request.POST.get("city-selector")
        
        for d in data_array:

            if d["city"] == selected_city:
                selected_city_country = d.get("country")
                selected_city_weather = d.get("weather")
                selected_city_weather_description = d.get("weather_description")
                selected_city_temperature = d.get("temperature")
                selected_city_weather_icon = d.get("weather_icon") 


    return render(request, "home.html", {
        "data": data_array, 
        "selected_city": selected_city,
        "selected_city_country": selected_city_country,
        "selected_city_weather": selected_city_weather,
        "selected_city_weather_description": selected_city_weather_description,
        "selected_city_temperature": selected_city_temperature,
        "selected_city_weather_icon": selected_city_weather_icon
        }
        )