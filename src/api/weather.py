from pprint import pprint

from src.api.accuweather_api import AccuWeatherAPI
from config.config import config


class Weather:
    def __init__(self):
        self.cached_data = {}

        self.api = AccuWeatherAPI()

    def get_weather(self, city_name: str, days_amount: int) -> dict:
        city_name = city_name.lower().strip()
        
        if config.bot.cache_enable and city_name in self.cached_data.keys(): 
            return self.cached_data[city_name]

        response_data = self.api.get_weather(city_name, days_amount=days_amount)
        response_data = response_data.get("DailyForecasts", [])

        weather_days = []
        for day in response_data:
            min_temperature = day.get("Temperature", {}).get("Minimum", {}).get("Value", 0)
            max_temperature = day.get("Temperature", {}).get("Maximum", {}).get("Value", 0)
            weather_data = {
                "date": day.get("Date"),
                "temperature": (min_temperature + max_temperature) / 2,
                "rain_probability": day.get("Day", {}).get("PrecipitationProbability", 0),
                "wind_speed": day.get("Day", {}).get("Wind", {}).get("Speed", {}).get("Value", 0)
            }
            weather_days.append(weather_data)

        self.cached_data[city_name] = weather_days

        return weather_days
