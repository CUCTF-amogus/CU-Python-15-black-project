import requests

from config.config import config


class AccuWeatherAPI:
    def __init__(self):
        pass

    def _get(self, url: str, params=None) -> dict:
        response = requests.get(url=url, params=params)
        print(response.url)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"incorrect request, response with status code {response.status_code}"
            )
        if not response.json():
            raise requests.exceptions.InvalidJSONError("no json in response")
        return response.json()

    def _get_location_key_by_text(self, location_name: str) -> str:
        url = f"{config.api.location_url}"
        params = {
            "apikey": config.api.api_key,
            "q": location_name,
        }
        response = self._get(url=url, params=params)[0]
        return response.get("Key", "")

    def _get_weather_by_location_key(self, location_key: str, days_amount: int) -> dict:
        url = f"{config.api.weather_url}/{days_amount}day/{location_key}"
        params = {
            "apikey": config.api.api_key,
            "details": "true",
        }
        return self._get(url=url, params=params)

    def get_weather(self, location_name: str, days_amount: int) -> dict:
        print(days_amount, "days_amount")
        location_key = self._get_location_key_by_text(location_name)
        weather_data = self._get_weather_by_location_key(location_key, days_amount=days_amount)
        return weather_data
