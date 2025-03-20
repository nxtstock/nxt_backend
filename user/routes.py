from fastapi import APIRouter
from startup.requests import UserData
from user.services import create_user_data_service

user_router = APIRouter(tags=["User"])


@user_router.post("/user-data")
def create_user_data(request: UserData):
    return create_user_data_service(request)
