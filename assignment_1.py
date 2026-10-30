print("Salam from our first class.")
import requests

# Mumbai coordinates
LATITUDE = 19.0760
LONGITUDE = 72.8777

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()
current = data["current"]

print("Today's Weather")
print("-" * 20)
print(f"Temperature: {current['temperature_2m']}°C")
print(f"Humidity: {current['relative_humidity_2m']}%")
print(f"Wind Speed: {current['wind_speed_10m']} km/h")
print(f"Weather Code: {current['weather_code']}")