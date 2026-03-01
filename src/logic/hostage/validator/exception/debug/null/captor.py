# src/logic/manifest/validator/exception/debug/captor.py

"""
Module: logic.manifest.validator.exception.debug.captor
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
    "PrisonerAlreadyHasHostageException",
]

from logic.system import NullException
from logic.hostage import HostageException


# ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
class PrisonerAlreadyHasHostageException(HostageException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
   1.  Indicate that a candidate failed its Hostage validation because the prisoner did not have its captor set.
    
    # PARENT:
        *   NullException
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PRISONER_DOES_NOT_HAVE_CAPTOR_SET_EXCEPTION"
    MSG = "Hostage validation failed: Captor was not set."