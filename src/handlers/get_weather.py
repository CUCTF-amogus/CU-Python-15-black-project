from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config.config import config
from src.keyboards.cities import GetWeatherCallbackData
from src.keyboards.weather_forecast_days import forecast_days_keyboard
from src.services import aio
from src.states.weather_states import InputCityState


router = Router()


@router.callback_query(GetWeatherCallbackData.filter())
async def get_weather(callback: types.CallbackQuery, state: FSMContext):
    await aio.clear_state_with_save_data(state)

    await callback.message.edit_text(
        text=config.messages.weather_forecast_days_message,
        reply_markup=forecast_days_keyboard,
    )
