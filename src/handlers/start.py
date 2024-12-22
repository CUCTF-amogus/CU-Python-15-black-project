from aiogram import Router, types
from aiogram.filters import CommandStart

from config.config import config


router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(config.messages.start_message)
