from fastapi import APIRouter
from startup.requests import UserOTPRequest
from signup.services import (
    verify_otp_service,
    generate_otp_service
)
login_router = APIRouter(tags=["Login"])


@login_router.get("/get-otp/{email}")
def generate_otp(email: str):
    return generate_otp_service(email)


@login_router.post("/verify-otp")
def verify_otp(request: UserOTPRequest):
    return verify_otp_service(request)
