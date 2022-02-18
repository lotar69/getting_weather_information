import requests
from pprint import pprint

API_Key = "257eb9b5d06997d2c288543f8e97d165"

city = input("Enter a city:\n")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)