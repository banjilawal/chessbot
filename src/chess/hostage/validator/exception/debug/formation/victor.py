# src/chess/hostage/validator/exception/debug/formation/victor
"""
Module: chess.hostage.validator.exception.debug.formation.victor
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# UNFORMED_TOKEN_CANNOT_BE_VICTOREXCEPTION #======================#
    "UnformedTokenCannotBeVictorException",
]

from chess.formation import FormationException
from chess.hostage import HostageManifestException


# ======================# UNFORMED_TOKEN_CANNOT_BE_VICTOR EXCEPTION #======================#
class UnformedTokenCannotBeVictorException(HostageManifestException, FormationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its HostageManifest validation because the victor did not have its
        formation set.

    # PARENT:
        *   HostageManifestException
        *   FormationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNFORMED_TOKEN_CANNOT_BE_VICTOR_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: The victor did not have its formation set."