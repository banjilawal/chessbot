# src/logic/hostage/validator/exception/debug/formation/victor
"""
Module: logic.hostage.validator.exception.debug.formation.victor
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# UNFORMED_TOKEN_CANNOT_BE_VICTOREXCEPTION #======================#
    "UnformedTokenCannotBeVictorException",
]

from logic.formation import FormationException
from logic.hostage import HostageException


# ======================# UNFORMED_TOKEN_CANNOT_BE_VICTOR EXCEPTION #======================#
class UnformedTokenCannotBeVictorException(HostageException, FormationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its Hostage validation because the victor did not have its
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
    ERR_CODE = "UNFORMED_TOKEN_CANNOT_BE_VICTOR_EXCEPTION"
    MSG = "Hostage validation failed: The victor did not have its formation set."