from .add_city import router as add_city_router
from .help import router as help_router
from .get_weather import router as get_weather_router
from .start import router as start_router
from .weather import router as weather_router

routers = [help_router, start_router, weather_router, get_weather_router, add_city_router]
