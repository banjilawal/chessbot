# src/chess/formation/validator/exception/debug/null.py

"""
Module: chess.formation.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONEREXCEPTION #======================#
    "UnformedTokenCannotBePrisonerException",
]

from chess.formation import FormationException
from chess.hostage import HostageManifestException



# ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONER EXCEPTION #======================#
class UnformedTokenCannotBePrisonerException(HostageManifestException, FormationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its HostageManifest validation because the prisoner did not have its
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
    ERROR_CODE = "UNFORMED_TOKEN_CANNOT_BE_PRISONER_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: The prisoner did not have its formation set."