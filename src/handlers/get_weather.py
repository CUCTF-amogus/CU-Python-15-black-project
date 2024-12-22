from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from config.config import config
from src.keyboards.cities import GetWeatherCallbackData
from src.keyboards.weather_forecast_days import forecast_days_keyboard, ForecastDaysCallbackData
from src.services import aio
from src import api


router = Router()


@router.callback_query(GetWeatherCallbackData.filter())
async def get_weather(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text(
        text=config.messages.weather_forecast_days_message,
        reply_markup=forecast_days_keyboard,
    )


@router.callback_query(ForecastDaysCallbackData.filter())
async def get_forecast(
    callback: types.CallbackQuery,
    callback_data: ForecastDaysCallbackData,
    state: FSMContext,
) -> None:
    await callback.message.edit_text(text=config.messages.weather_requesting_data_message)

    state_data = await state.get_data()
    cities = state_data.get("cities", [])
    weatherAPI = api.Weather()

    text = ""

    for city in [cities[0]]:
        try:
            forecast = weatherAPI.get_weather(city, days_amount=callback_data.amount)
            if not forecast:
                text += f"Не удалось получить данные о погоде в городе {city}\n"
                continue

            text += f"city: {city}\n"
            for day in forecast:
                text += (
                    f"Date: {day.get('date', 'Не известно')}\n"
                    f"Temperature: {day.get('temperature', 'Не известно')}\n"
                    f"Rain probability: {day.get('rain_probability', 'Не известно')}\n"
                    f"Wind speed: {day.get('wind_speed', 'Не известно')}\n"
                    f"\n"
                )
        except Exception as e:
            print(e)
            text += f"Не удалось получить данные о погоде в городе {city}\n"

    await callback.message.edit_text(text=text)
