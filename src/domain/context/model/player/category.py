# src/domain/context/model/player/category.py

"""
Module: domain.context.model.player.category
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class PlayerType(Enum):
    HUMAN = auto(),
    MACHINE = auto(),