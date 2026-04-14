# src/setup/log/__init__.py

"""
Module: setup.log.__init__
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

import logging



# =========== SETUP.LOG PACKAGE ===========#

# Packages

# Modules
from .mode import LogLevelMode
from .level import LogLevelSetter


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