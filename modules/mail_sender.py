import random
import smtplib
from time import time
from os import getenv
from loguru import logger
from datetime import datetime
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SMTP_SENDER_EMAIL = getenv("SMTP_SENDER_EMAIL")
OTP_EXPIRY_TIME = int(getenv("OTP_EXPIRY_TIME"))
SMTP_SENDER_APP_PASSWORD = getenv("SMTP_SENDER_APP_PASSWORD")


def generate_otp():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    otp = ''.join(random.choice(timestamp) for _ in range(4))
    timestamp = time()
    expiry_time = timestamp + (OTP_EXPIRY_TIME * 60)
    return otp, expiry_time


def send_mail(user_mail):
    try:
        otp, expiry_time = generate_otp()
        subject = "Your OTP for Verification"
        message = MIMEMultipart()
        message["From"] = SMTP_SENDER_EMAIL
        message["To"] = user_mail
        message["Subject"] = subject

        body = f"Your OTP is: {otp}"
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_SENDER_EMAIL, SMTP_SENDER_APP_PASSWORD)
            server.sendmail(SMTP_SENDER_EMAIL, user_mail, message.as_string())

        return {
            "otp": otp,
            "expiry_time": expiry_time
        }

    except Exception as e:
        logger.info(f"Mail Send Error: {e}")
        return False
