import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import config
from src.handlers import routers
from src.middlewares import MessageInPrivateMiddleware


logger = logging.getLogger(__name__)


async def main():
    load_dotenv()
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Start bot")

    bot: Bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode='HTML'),
    )

    dp: Dispatcher = Dispatcher()

    dp.include_routers(*routers)

    dp.message.outer_middleware(MessageInPrivateMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info('Bot stopped')
