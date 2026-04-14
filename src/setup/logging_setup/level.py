# src/setup/level.py

"""
Module: setup.level
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

from __future__ import annotations

import logging

from setup import LogLevelMode


class LogLevelSetter:
    DEFAULT_LOGGER = "AppLog"
    DEFAULT_LEVEL = LogLevelMode.DEBUG
    
    _logger: logging.Logger
    _log_level: LogLevelMode

    
    def __init__(
            self,
            logger: logging.Logger = DEFAULT_LOGGER,
            log_level: LogLevelMode = DEFAULT_LEVEL,
    ):
        self._logger = logger
        self._log_level = log_level
        
    @property
    def logger(self) -> logging.Logger:
        return self._logger
    
    @property
    def log_level(self) -> LogLevelMode:
        return self._log_level
    
    @log_level.setter
    def log_level(self, log_level: LogLevelMode):
        self._log_level = log_level
    
    def log_error(self, error: Exception):
        # logger = logging.getLogger("AppLog")
        
        if self._log_level == LogLevelMode.DEBUG:
            self._logger.exception(msg=error, exc_info=error)
            raise RuntimeError(error)
        else:
            self._logger.warning(f"[WARNING]: {str(error)}")