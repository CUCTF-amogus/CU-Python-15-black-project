from .help import router as help_router
from .start import router as start_router
from .weather import router as weather_router

routers = [help_router, start_router, weather_router]
