# src/domain/context/model/token/context.py

"""
Module: domain.context.model.token.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    COMBATANT_TOKEN = auto(),
    KING_TOKEN = auto(),
    PAWN_TOKEN = auto(),