from loguru import logger
from .alchemy import Base

try:  # Users/Employee Tables
    table = Base.classes.test

except Exception as err:
    logger.error("error while creating models - {}".format(err))
