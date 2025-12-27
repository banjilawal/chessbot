# src/chess/arena/service/exception/debug/collision/color.py

"""
Module: chess.arena.service.exception.debug.collision.color
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
    "ArenaSlotAlreadyOccupiedException",
]

from chess.arena import ArenaException


# ======================# ARENA_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
class ArenaSlotAlreadyOccupiedException(ArenaException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a slot color slot for a team is already occupied.

    # PARENT:
        *   ArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_SLOT_ALREADY_OCCUPIED_ERROR"
    DEFAULT_MESSAGE = "A team has already been assigned that color slot."