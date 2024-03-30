import requests

base_url = "http://127.0.0.1:5000/weather/"
city = "New York"
response = requests.get(base_url + city)

if response.status_code == 200:
    data = response.json()
    city_weather = data.get(city, {})
    temperature = city_weather.get('temperature', 'No temperature data')
    condition = city_weather.get('condition', 'No condition data')
    print(f"Weather in {city}: {temperature}, {condition}")
else:
    print("Failed to retrieve data.")
