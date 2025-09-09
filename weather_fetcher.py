import requests

def get_weather(city):
    # You can use the Open-Meteo API, which does not require authentication:
    # We'll use the /forecast endpoint to get current temperature.
    # Get latitude/longitude for city using Open-Meteo Geocoding API.
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_resp = requests.get(geo_url)
    geo_data = geo_resp.json()
    if not geo_data.get("results"):
        print(f"Could not find location for city: {city}")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Fetch current weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_resp = requests.get(weather_url)
    weather_data = weather_resp.json()
    curr_weather = weather_data.get("current_weather")
    if not curr_weather:
        print("Could not fetch current weather.")
        return

    temperature = curr_weather["temperature"]
    windspeed = curr_weather["windspeed"]
    weather_code = curr_weather["weathercode"]

    print(f"Current weather in {city}:")
    print(f"  Temperature: {temperature}°C")
    print(f"  Windspeed: {windspeed} km/h")
    print(f"  Weather Code: {weather_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
