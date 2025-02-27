from .bootstrap import app
from .routes.home import router as home_router


app.include_router(home_router)
