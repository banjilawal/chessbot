# src/domain/model/searchable/state/arena/state.py

"""
Module: domain.model.searchable.state.arena.state
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""
from enum import Enum, auto


class ArenaState(Enum):
    NO_TOKEN_OPENED = auto(),
    OPENING_MOVE_LAUNCHED = auto()