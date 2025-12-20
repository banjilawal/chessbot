# src/chess/arena/number_bounds_validator/exception/null.py

"""
Module: chess.game.arena.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from chess.system import NullException
from chess.arena import InvalidArenaException

__all__ = [
    # ======================# NULL_ARENA EXCEPTION #======================#
    "NullArenaException",
]


# ======================# NULL_ARENA EXCEPTION #======================#
class NullArenaException(InvalidArenaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Arena validation candidate is null.
    2.  Raised if an entity, method or operation requires a Arena but receives null instead.

    # PARENT:
        *   NullArenaException
        *   InvalidArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ARENA___ERROR"
    DEFAULT_MESSAGE = "Arena cannot be null."