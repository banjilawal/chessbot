# src/setup/mode.py

"""
Module: setup.mode
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

from __future__ import annotations

from enum import Enum, auto


class LogLevelMode(Enum):
  DEBUG = auto()
  PRODUCTION = auto()