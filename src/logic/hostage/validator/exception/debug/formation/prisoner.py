# src/logic/hostage/validator/exception/debug/formation/prisoner
"""
Module: logic.hostage.validator.exception.debug.formation.prisoner
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONER EXCEPTION #======================#
    "UnformedTokenCannotBePrisonerException",
]

from logic.formation import FormationException
from logic.hostage import HostageException



# ======================# UNFORMED_TOKEN_CANNOT_BE_PRISONER EXCEPTION #======================#
class UnformedTokenCannotBePrisonerException(HostageException, FormationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its Hostage validation because the prisoner did not have its
        formation set.

    # PARENT:
        *   HostageException
        *   FormationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNFORMED_TOKEN_CANNOT_BE_PRISONER_EXCEPTION"
    MSG = "Hostage validation failed: The prisoner did not have its formation set."