# src/chess/team/prisoner/exception/insertion/duplicate.py

"""
Module: chess.team.prisoner.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ENEMY_ALREADY_CAPTURED EXCEPTION #======================#
    "EnemyAlreadyCapturedException",
]

from chess.team import HostageServiceException


# ======================# ENEMY_ALREADY_CAPTURED EXCEPTION #======================#
class EnemyAlreadyCapturedException(HostageServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a prisoner member failed because the token was already present.

    # PARENT:
        *   HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENEMY_ALREADY_CAPTURED_ERROR"
    DEFAULT_MESSAGE = "Adding prisoner failed: The enemy was already a prisoner."