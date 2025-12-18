# src/chess/arena/validator/exception/capacity.py

"""
Module: chess.game.arena.validator.exception.capacity
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import BoundsException
from chess.arena import InvalidArenaException


class TooManyTeamsInArenaException(InvalidArenaException, BoundsException):
    """Raised when trying to have more than two teams in the arena."""
    ERROR_CODE = "PLAYING_FIELD_OVER_CAPACITY_ERROR"
    DEFAULT_MESSAGE = "Cannot have more than two teams in the arena."