# src/chess/token/model/concrete/combatant/pawn/exception.py

"""
Module: chess.token.model.concrete.combatant.pawn.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# PAWN_TOKEN EXCEPTION #======================#
    "PawnTokenException",
]

from chess.token import TokenException


# ======================# PAWN_TOKEN EXCEPTION #======================#
class PawnTokenException(TokenException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent and catchall for exception specific to PawnToken instances.

    # PARENT:
        *   TokenException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_TOKEN_ERROR"
    DEFAULT_MESSAGE = "PawnToken raised an exception."