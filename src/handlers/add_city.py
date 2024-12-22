from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from src.keyboards.cities import AddCityCallbackData
from src.states.weather_states import InputCityState


router = Router()


@router.callback_query(AddCityCallbackData.filter())
async def add_city(
        callback: types.CallbackQuery,
        callback_data: AddCityCallbackData,
        state: FSMContext,
):
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.set_state(InputCityState.city)
    await state.update_data(insert_index=callback_data.index)
    await callback.message.answer("Введите город:")
