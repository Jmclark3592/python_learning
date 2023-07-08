#! python3
# API key a1176144641989f43e6290cb3f31cc8c

import json, requests, sys, os

api = os.getenv("weather")


if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])

url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&appid=a1176144641989f43e6290cb3f31cc8c"
response = requests.get(url)

weatherData = json.loads(response.text)

w = weatherData["list"]
print("Current weather in %s:" % (location))
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])

# why is flake8 and blackout not running? well not they are today..
# can't seem to echo the $weather (api key) variable I made
# why is this code not working?
