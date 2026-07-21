# src/util/logging/setup/level/__init__.py

"""
Module: util.logging.setup.level.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging


# =========== UTIL.LOGGING.SETUP.LEVEL PACKAGE ===========#

# Packages


# Modules
from .mode import LogLevelMode
from .util import LogLevelSetter


# Set default log level and logger name
DEFAULT_LOGGER_NAME = "chessbot"
DEFAULT_LOG_LEVEL = LogLevelMode.DEBUG  # Can toggle between DEBUG/PRODUCTION here

# Configuring the root logger
logging.basicConfig(
    level=logging.DEBUG if DEFAULT_LOG_LEVEL == LogLevelMode.DEBUG else logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Define the central logger
log = logging.getLogger(DEFAULT_LOGGER_NAME)
log.info(f"Logger initialized with level: {DEFAULT_LOG_LEVEL.name}")