from dotenv import load_dotenv
import json
import os
from pyowm import OWM

from .reporter import Reporter

class WeatherStats():
    def __init__(self):
        load_dotenv()
        owm = OWM(os.getenv("OWM_APIKEY"))
        self.mgr = owm.weather_manager()
        reg = owm.city_id_registry()
        self.loc = reg.locations_for(os.getenv("CITY"), state=os.getenv("STATE"), country=(os.getenv("COUNTRY")))
        if len(self.loc) > 1:
            self.loc = self.loc[0]
        self.update_stats()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def get_weather(self):
        oc = self.mgr.one_call(lat=self.loc.lat, lon=self.loc.lon)
        return oc.current

    def update_stats(self):
        current_weather = self.get_weather()
        self.uv_index = current_weather.uvi
        self.heat_index = current_weather.heat_index
        self.status = current_weather.detailed_status
        self.tempC = current_weather.temperature('celsius')
        self.tempF = current_weather.temperature('fahrenheit')
        self.humidity = current_weather.humidity
        self.cloudpct = current_weather.clouds
        # Returned in Kelvin
        self.dewpoint = round(((current_weather.dewpoint-273)*1.8)+32, 2)
        self.snow = current_weather.snow
        self.rain = current_weather.rain

    async def report(self):
        data = {
            "UV Index": self.uv_index,
            "Heat Index": self.heat_index,
            "Detailed Status": self.status,
            "Temp (C)": self.tempC['temp'],
            "Temp (F)": self.tempF['temp'],
            "Humidity": self.humidity,
            "Dew Point": self.dewpoint,
            "Cloud Cover": self.cloudpct,
            "Snow": self.snow,
            "Rain": self.rain
        }
        Reporter(title="Weather Status", data=data).report()