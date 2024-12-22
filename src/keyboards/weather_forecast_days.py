from aiogram.utils.keyboard import CallbackData, InlineKeyboardMarkup, InlineKeyboardButton

from src.messages import messages


class ForecastDaysCallbackData(CallbackData, prefix="forecast_days"):
    amount: int


forecast_days_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text=str(days_amount),
            callback_data=ForecastDaysCallbackData(amount=days_amount).pack(),
        )
    ] for days_amount in (5, 10, 15)
])