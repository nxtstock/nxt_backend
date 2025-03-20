from os import getenv
from json import loads
from loguru import logger
from dotenv import load_dotenv
from startup.models import IPONames

load_dotenv()
IPO_STOP_WORDS = loads(getenv("IPO_STOP_WORDS"))


def ipo_saving(provider_name, ipo_names):
    try:
        for ipo_name in ipo_names:
            for word in IPO_STOP_WORDS:
                if word.lower() in ipo_name.lower():
                    continue
                IPONames(
                    ipo_name=ipo_name,
                    ipo_provider=provider_name
                ).save()

    except Exception as e:
        logger.info(f"IPO Saving Error: {e}")
