# src/chess/occupant/context/finder/exception/debug/id.py

"""
Module: chess.occupant.context.finder.exception.debug.id
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    "TokenSearchIdCollisionException",
]

from chess.token import Token
from chess.system import CollisionException


# ======================# TOKEN_SEARCH_ID_COLLISION EXCEPTION #======================#
class TokenSearchIdCollisionException(Token, CollisionException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That search by Token.id which should produce either a single match or none returned
        different tokens with the same id.

    # PARENT:
        *   TokenException
        *   CollisionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SEARCH_ID_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "TokenSearch failed: There was id collision. The results contain different tokens that share an id."
    )