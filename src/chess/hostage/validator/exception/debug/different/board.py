# src/chess/prisoner/validator/exception/debug/different/board.py

"""
Module: chess.prisoner.validator.exception.debug.different.board
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
    "VictorAndPrisonerConflictingBoardException",
]

from chess.hostage import HostageManifestException

# ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
class VictorAndPrisonerConflictingBoardException(HostageManifestException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its HostageManifest validation because the victor and prisoner
        were on different boards.

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
    DEFAULT_MESSAGE = "HostageManifest validation failed: The victor can only capture enemies on its own board."