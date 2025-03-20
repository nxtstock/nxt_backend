from user.routes import user_router
from signup.routes import login_router


def initialize_routes(app):
    app.include_router(user_router, prefix="/api/v1/nxt")
    app.include_router(login_router, prefix="/api/v1/nxt")
