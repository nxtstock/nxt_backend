from os import getenv
from loguru import logger
from dotenv import load_dotenv
from startup.models import IPOProviders
from modules.ipo_saver import ipo_saving
from requests_html import AsyncHTMLSession
from modules.error_handler import value_error_exception_handler

load_dotenv()
KFINTECH_CLASS_NAME = getenv("KFINTECH_CLASS_NAME")


async def kfintech_ipo_extracter(
        provider_name="https://ris.kfintech.com/ipostatus/"
):
    try:
        ipo_extracter_obj = IPOProviders.objects(
            provider_name=provider_name
        ).get()

        final_ipo_name = []

        for url in ipo_extracter_obj.provider_source:
            session = AsyncHTMLSession()

            response = await session.get(url)
            elements = response.html.find(KFINTECH_CLASS_NAME)

            for element in elements:
                ipo_name = element.text
                final_ipo_name.extend(ipo_name.split("\n"))

        ipo_saving(
            provider_name,
            set(final_ipo_name)
        )

    except Exception as e:
        logger.info(f"KFINTECH Extracter Error: {e}")
        return value_error_exception_handler(e)
