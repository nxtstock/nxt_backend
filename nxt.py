from uvicorn import run
from fastapi import FastAPI
from startup.routes import initialize_routes
from modules.database import connect_to_mongo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

connect_to_mongo()
initialize_routes(app)


if __name__ == "__main__":
    run(
        app,
        host="0.0.0.0",
        port=8000
    )
