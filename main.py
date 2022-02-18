import requests
from pprint import pprint

API_Key = input("Enter your open weather map API Key:")

city = input("Enter a city:\n")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+str(API_Key)+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)