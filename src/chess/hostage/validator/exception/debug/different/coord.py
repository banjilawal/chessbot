# src/chess/prisoner/validator/exception/debug/different/coord.py

"""
Module: chess.prisoner.validator.exception.debug.different.coord
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_COORDS EXCEPTION #======================#
    "VictorAndPrisonerConflictingCoordException",
]

from chess.hostage import HostageManifestException


# ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_COORDS EXCEPTION #======================#
class VictorAndPrisonerConflictingCoordException(HostageManifestException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its HostageManifest validation because the victor and prisoner were on
        different coords.

    # PARENT:
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VICTOR_AND_PRISONER_ON_DIFFERENT_COORDS_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: The victor can only capture enemies on its own coord."