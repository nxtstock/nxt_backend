from loguru import logger
from datetime import datetime
from startup.models import LoginOTP
from modules.mail_sender import send_mail
from modules.error_handler import value_error_exception_handler


def generate_otp_service(
        email
):
    try:
        otp_response = send_mail(email)

        if not otp_response:
            return value_error_exception_handler(
                "Error Sending Mail"
            )

        login_otp_obj = LoginOTP.objects(
            user_email=email
        ).first()

        if login_otp_obj:
            login_otp_obj.update(
                set__otp=otp_response.get("otp"),
                set__expiry_time=otp_response.get("expiry_time"),
                set__updatedAt=datetime.now()
            )
            return {
                "Successfully Resened OTP Mail"
            }

        print(otp_response)

        LoginOTP(
            user_email=email,
            otp=otp_response.get("otp"),
            expiry_time=otp_response.get("expiry_time")
        ).save()

        return {
            "message": "Successfully Sent OTP Mail"
        }

    except Exception as e:
        logger.info(f"Generate OTP Error: {e}")
        return value_error_exception_handler(e)


def verify_otp_service(request):
    try:
        login_otp_obj = LoginOTP.objects(
            user_email=request.email
        ).first()

        if not login_otp_obj:
            return {
                f"No OTP Found For {request.email}"
            }

        if request.otp != login_otp_obj.otp:
            return {
                "OTP Doesn't Match"
            }

        return {
            "OTP Successfully Verified"
        }

    except Exception as e:
        logger.info(f"Verify OTP Error: {e}")
        return value_error_exception_handler(e)
