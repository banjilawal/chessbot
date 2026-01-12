# src/chess/owner/model/order.py

"""
Module: chess.owner.model.order
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from enum import Enum, auto


class PlayerOrder(Enum):
  WHITE_FIRST = auto()
  BLACK_SECOND = auto()