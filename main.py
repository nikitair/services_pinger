from loguru import logger
import time
import os
import requests

# set timezone to UTC
os.environ['TZ'] = 'UTC'
time.tzset()


logger.add("logs.log",
           rotation="500 MB",
           format="{time:YYYY-MM-DD HH:mm:ss} UTC | {level} | {message}",
           level="DEBUG",
           compression="zip")


logger.info("SYSTEM SET UP")

services = [
    "https://textingduncan.onrender.com"
]


while True:
    for service in services:
        logger.info(f"PING - ({service})")
        try:
            response = requests.get(service)
            status_code = response.status_code
            logger.info(f"STATUS CODE - ({status_code}) | RESPONSE - ({response.json()})")
            
            if status_code in (200, 201):
                logger.info("SUCCESSFUL PING")
            else:
                logger.error(f"!!! ERROR PINGING API - ({response.text})")
            
        except Exception as ex:
            logger.error(f"!!! Exception - {ex}")
        finally:
            time.sleep(5)
