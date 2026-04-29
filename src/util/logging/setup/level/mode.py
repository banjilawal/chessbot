# src/util/logging/setup/level/mode.py

"""
Module: util.logging.setup.level.mode
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from enum import Enum, auto


class LogLevelMode(Enum):
  DEBUG = auto()
  PRODUCTION = auto()