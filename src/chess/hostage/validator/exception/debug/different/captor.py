# src/chess/hostage/validator/exception/debug/different/board.py

"""
Module: chess.hostage.validator.exception.debug.different.board
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
    "PrisonerCapturedByDifferentEnemyException",
]

from chess.hostage import HostageManifestException


# ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
class PrisonerCapturedByDifferentEnemyException(HostageManifestException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its HostageManifest validation because the prisoner had a different captor.

    # PARENT:
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: the prisoner was captured by a different friend."