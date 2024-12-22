import logging
from dataclasses import dataclass

from dotenv import load_dotenv

from .base import getenv
from src.messages import messages


# logging
def init_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("app.log")


@dataclass
class Bot:
    token: str


@dataclass
class Messages:
    start_message: str
    help_message: str
    weather_start_city_message: str
    weather_end_city_message: str
    weather_city_added_message: str
    weather_current_roadmap_message: str
    weather_get_forecast_message: str
    weather_forecast_days_message: str


@dataclass
class Config:
    bot: Bot
    messages: Messages


def load_config() -> Config:
    load_dotenv()
    
    return Config(
        bot=Bot(
            token=getenv("AIOGRAM_TOKEN"),
        ),
        messages=Messages(
            start_message=messages.start_message,
            help_message=messages.help_message,
            weather_start_city_message=messages.weather_start_city_message,
            weather_end_city_message=messages.weather_end_city_message,
            weather_city_added_message=messages.weather_city_added_message,
            weather_current_roadmap_message=messages.weather_current_roadmap_message,
            weather_get_forecast_message=messages.weather_get_forecast_message,
            weather_forecast_days_message=messages.weather_forecast_days_message,
        ),
    )


config: Config = load_config()
