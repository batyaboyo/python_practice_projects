import requests

API_KEY = "45b01a7f6a9893cc9370a6fd91f105fb"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def display_current_weather(data):
    if data:
        print("\nCurrent Weather:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No weather data available.")

def get_forecast_data(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching forecast data.")
        return None

def display_five_day_forecast(data):
    if data:
        print("\nFive-Day Forecast:")
        for forecast in data['list']:
            print(f"\nDate: {forecast['dt_txt']}")
            print(f"Temperature: {forecast['main']['temp']}°C")
            print(f"Humidity: {forecast['main']['humidity']}%")
            print(f"Wind Speed: {forecast['wind']['speed']} m/s")
    else:
        print("No forecast data available.")

def weather():
    city = input("Enter city name: ")
    current_weather_data = get_weather_data(city)
    display_current_weather(current_weather_data)
    
    forecast_data = get_forecast_data(city)
    display_five_day_forecast(forecast_data)


weather()