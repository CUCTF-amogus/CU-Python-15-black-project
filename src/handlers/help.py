from aiogram import Router, types
from aiogram.filters import Command

from config.config import config


router = Router()


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(config.messages.help_message)
