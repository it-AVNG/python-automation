#! python3
'''
prints the weather for a location from the command line
'''
import os
import json, requests, sys
from dotenv import load_dotenv
import pprint
#load environment data
load_dotenv()
APPID_w = os.environ.get('APIID_w')
APPID_f = os.environ.get('APIID_f')
# compute location from commandline arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])


# TODO: Download the JSON from open Weather map .org API
url_w = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID_w)
response_weather = requests.get(url_w)
response_weather.raise_for_status()

url_f = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (location, APPID_w)
response_forecast = requests.get(url_f)
response_forecast.raise_for_status()
#Json will be stored in response.text
# TODO: Load JSON data into python variable
weatherData = json.loads(response_weather.text)
pprint.pprint(weatherData)
w = dict(weatherData)
print('Currently in %s:' % (location))
print('The weather: %s'% (w['weather'][0]['description']))

forecast_data = json.loads(response_forecast.text)
pprint.pprint(forecast_data)

