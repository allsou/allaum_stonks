import logging
import os
from logging.config import fileConfig

fileConfig("settings/logging_config.ini")
LOGGER = logging.getLogger("sLogger")

DEFAULT_SCREENING = os.getenv(
    "DEFAULT_SCREENING", "connections.fundamentus.Fundamentus"
)
