# src/chess/token/model/concrete/combatant/classification.py

"""
Module: chess.token.model.concrete.combatant.classification
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto

class CombatantReadinessEnum(Enum):
    FREE = auto(),
    CAPTURE_ACTIVATED = auto(),
    ISSUED_HOSTAGE_MANIFEST = auto(),
    MANIFESTED_HOSTAGE_OFF_BOARD = auto(),
    NOT_INITIALIZED = auto(),
    