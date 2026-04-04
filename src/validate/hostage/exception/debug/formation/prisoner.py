# src/logic/hostage/validation/exception/debug/formation/prisoner
"""
Module: logic.hostage.validation.exception.debug.formation.prisoner
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONER EXCEPTION #======================#
    "UnformedTokenCannotBePrisonerException",
]

from catalog.formation import FormationException
from model.hostage import HostageException



# ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONER EXCEPTION #======================#
class UnformedTokenCannotBePrisonerException(HostageException, FormationException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank failed its Hostage validation because the prisoner did not have its
        formation set.

    Super Class:
        *   HostageException
        *   FormationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNFORMED_TOKEN_CANNOT_BE_PRISONER_EXCEPTION"
    MSG = "Hostage validation failed: The prisoner did not have its formation set."