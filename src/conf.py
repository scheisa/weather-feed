api_key = "ab9e7b341c1a4143b03175931230908"
url = "http://api.weatherapi.com/v1/forecast.json?key=ab9e7b341c1a4143b03175931230908&q=Konotop&days=1&aqi=yes&alerts=yes"


def define_data(data):
    global last_updated
    last_updated = data["current"]["last_updated"]

    # location data
    global city_name
    city_name = data["location"]["name"]
    global region_name
    region_name = data["location"]["region"]
    global country_name
    country_name = data["location"]["country"]

    # forecast data
    global date
    date = data["forecast"]["forecastday"][0]["date"]
    global maxtemp_c
    maxtemp_c = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
    global mintemp_c
    mintemp_c = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    global avgtemp_c
    avgtemp_c = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    global maxwind_kph
    maxwind_kph = data["forecast"]["forecastday"][0]["day"]["maxwind_kph"]

    # chances
    global will_it_rain
    will_it_rain = data["forecast"]["forecastday"][0]["day"]["daily_will_it_rain"]
    global chance_of_rain
    chance_of_rain = data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
    global will_it_snow
    will_it_snow = data["forecast"]["forecastday"][0]["day"]["daily_will_it_snow"]
    global chance_of_snow
    chance_of_snow = data["forecast"]["forecastday"][0]["day"]["daily_chance_of_snow"]

    # weather
    global weather_avg
    weather_avg = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
    global weather_avg_icon
    weather_avg_icon = data["forecast"]["forecastday"][0]["day"]["condition"]["icon"].replace("//", "https://")

    # astro
    global sunrise
    sunrise = data["forecast"]["forecastday"][0]["astro"]["sunrise"]
    global sunset
    sunset = data["forecast"]["forecastday"][0]["astro"]["sunset"]
    global moonrise
    moonrise = data["forecast"]["forecastday"][0]["astro"]["moonrise"]
    global moonset
    moonset = data["forecast"]["forecastday"][0]["astro"]["moonset"]
    global moon_phase
    moon_phase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

    global hour
    hour = data["forecast"]["forecastday"][0]["hour"]

    global main_hours
    main_hours = [hour[i] for i in range(0, len(hour), 3)]
    main_hours.append(hour[-1])

    global hour_data
    hour_data = {}
    for i in range(len(main_hours)):
        hour_data[f"{main_hours[i]['time']}"] = {
            "time": main_hours[i]["time"],
            "temp_c": main_hours[i]["temp_c"],
            "feels_like": main_hours[i]["feelslike_c"],
            "desc": main_hours[i]["condition"]["text"],
            "desc_icon": main_hours[i]["condition"]["icon"].replace("//", "https://"),
            "wind_kph": main_hours[i]["wind_kph"],
            "wind_dir": main_hours[i]["wind_dir"],
            "will_it_rain": main_hours[i]["will_it_rain"],
            "chance_of_rain": main_hours[i]["chance_of_rain"],
            "will_it_snow": main_hours[i]["will_it_snow"],
            "chance_of_snow": main_hours[i]["chance_of_snow"],
        }
