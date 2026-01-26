# src/chess/team/prisoner/exception/insertion/king.py

"""
Module: chess.team.prisoner.exception.insertion.king
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import HostageServiceException

__all__ = [
    # ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
    "CannotCaptureKingException",
]


# ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
class CannotCaptureKingException(HostageServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that adding a occupant to the prisoners failed because it was a KingToken instead of a CombatantToken

    # PARENT:
        *   HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "KING_CANNOT_BE_CAPTURED"
    DEFAULT_MESSAGE = "Adding prisoner failed: A KingToken cannot be captured."