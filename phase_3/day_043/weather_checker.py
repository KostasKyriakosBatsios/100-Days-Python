# Day 43 20/10/26

import re
import requests

URL_SEARCH = "https://geocoding-api.open-meteo.com/v1/search"
URL_FORECAST = "https://api.open-meteo.com/v1/forecast"
PATTERN_STRING = r"[A-Za-z,\s]+"

WEATHER_CODES = {
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
	"45": "Fog",
	"48": "Depositing rime fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"
}

def main():
    print("========== WEATHER CHECKER ==========")
    
    while True:
        num = get_int("\n1. Check current weather.\n2. Exit\n\nChoose: ")
        
        if num == 2:
            break
        
        forecast_town()
    
    print("\nGoodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            
            if n == 1 or n == 2:
                return n
                
            print("\nChoose either 1 or 2!")
        except ValueError:
            print("\nOnly integer numbers!")


def forecast_town():
    t = ""
    
    while not re.fullmatch(PATTERN_STRING, t):
        t = input("\nTown: ")
    
    town = get_request(URL_SEARCH + f"?name={t}&count=10&language=en&format=json")
    
    if town is None or not town.get("results"):
        return print("\nNo town found!")
    
    res = town["results"][0]
    lat, lon = res["latitude"], res["longitude"]
    town_fc = get_request(URL_FORECAST + f"?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code")
    
    if town_fc is None or not town_fc.get("current"):
        return print("\nNo info found!")
    
    print(
            f"Temperature: {town_fc['current']['temperature_2m']} °C\n"
            f"Feels like: {town_fc['current']['apparent_temperature']} °C\n"
            f"Humidity: {town_fc['current']['relative_humidity_2m']}%\n"
            f"Wind speed: {town_fc['current']['wind_speed_10m']} km/h"
    )

    for k in WEATHER_CODES.keys():
        if k == str(town_fc["current"]["weather_code"]):
            print(f"Weather code: {town_fc['current']['weather_code']} ({WEATHER_CODES[k]})")
            break


def get_request(url):
    try:
        rsp = requests.get(url, timeout=5)
        rsp.raise_for_status()
    except requests.RequestException as e:
        print(f"\n{e}")
        return None
    
    if rsp.status_code == 200:
        return rsp.json()
    else:
        print(f"\nError: {rsp.status_code}")
        return None


main()
