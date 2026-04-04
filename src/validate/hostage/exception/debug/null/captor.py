# src/logic/manifest/validation/exception/debug/captor.py

"""
Module: logic.manifest.validation.exception.debug.captor
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
    "PrisonerAlreadyHasHostageException",
]

from system import NullException
from model.hostage import HostageException


# ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
class PrisonerAlreadyHasHostageException(HostageException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
   1.  Indicate that a rank failed its Hostage validation because the prisoner did not have its captor set.
    
    Super Class:
        *   NullException
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PRISONER_DOES_NOT_HAVE_CAPTOR_SET_EXCEPTION"
    MSG = "Hostage validation failed: Captor was not set."