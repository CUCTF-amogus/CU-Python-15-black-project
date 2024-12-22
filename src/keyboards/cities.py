from aiogram.utils.keyboard import CallbackData, InlineKeyboardMarkup, InlineKeyboardBuilder

from src.messages import messages


class AddCityCallbackData(CallbackData, prefix="add_city"):
    index: int


class ChooseCityCallbackData(CallbackData, prefix="choose_city"):
    city: str


class GetWeatherCallbackData(CallbackData, prefix="get_weather"):
    pass


def get_cities_keyboard(cities: list[str]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="+", callback_data=AddCityCallbackData(index=0).pack())

    for city_index, city in enumerate(cities):
        keyboard.button(text=city, callback_data=ChooseCityCallbackData(city=city).pack())
        keyboard.button(text="+", callback_data=AddCityCallbackData(index=city_index).pack())

    keyboard.button(text=messages.weather_get_forecast_message, callback_data=GetWeatherCallbackData().pack())
    keyboard.adjust(1)
    return keyboard.as_markup()
