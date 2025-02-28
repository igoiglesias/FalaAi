from .bootstrap import app
from .routes.home import router as home_router
from .routes.admin import router as admin_router


app.include_router(home_router)
app.include_router(admin_router)
