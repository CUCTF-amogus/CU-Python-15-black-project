from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config.config import config
from src.keyboards.cities import get_cities_keyboard
from src.services import aio
from src.states.weather_states import InputCityState


router = Router()


@router.message(Command("weather"))
async def weather(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(config.messages.weather_start_city_message)
    await state.update_data(cities=[], insert_index=0)
    await state.set_state(InputCityState.city)


@router.message(InputCityState.city, F.text)
async def input_city(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    cities = state_data.get("cities", [])
    insert_index = state_data.get("insert_index", 0)

    city = message.text

    cities.insert(insert_index, city)
    await state.update_data(cities=cities)

    if len(cities) == 1:
        await message.answer(config.messages.weather_end_city_message)
        await state.set_state(InputCityState.city)
        await state.update_data(insert_index=1)
        return
    
    await aio.clear_state_with_save_data(state)
    await message.reply(
        text=f"{config.messages.weather_city_added_message.format(city)}\n{config.messages.weather_current_roadmap_message}",
        reply_markup=get_cities_keyboard(cities),
    )
