from aiogram.fsm.state import State, StatesGroup


class InputCityState(StatesGroup):
    city = State()
