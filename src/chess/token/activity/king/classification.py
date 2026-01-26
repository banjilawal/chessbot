# src/chess/occupant/classification/activity/king/classification.py

"""
Module: chess.occupant.classification.activity.king.classification
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto

class KingReadinessEnum(Enum):
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto(),
    NOT_INITIALIZED = auto(),
