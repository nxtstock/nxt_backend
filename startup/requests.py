from pydantic import BaseModel


class UserOTPRequest(BaseModel):
    otp: int
    email: str


class UserData(BaseModel):
    account_type: str
    user_name: str
    pan_card: str
    dp_id: str = None
    client_id: str
    upi_id: str
