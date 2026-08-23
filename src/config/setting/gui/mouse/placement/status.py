# src/config/setting/gui/mouse/placement/status.py

"""
Module: config.setting.gui.mouse.placement.status
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto

class MousePlacementStatus(Enum):
  PLACED = auto()
  BLOCKED = auto()
  RELEASED = auto()
  INVALID = auto()