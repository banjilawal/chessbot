# src/chess/manifest/validator/exception/debug/captor.py

"""
Module: chess.manifest.validator.exception.debug.captor
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
    "PrisonerAlreadyHasHostageManifestException",
]

from chess.system import NullException
from chess.hostage import HostageManifestException


# ======================# PRISONER_DOES_NOT_HAVE_CAPTOR_SET EXCEPTION #======================#
class PrisonerAlreadyHasHostageManifestException(HostageManifestException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
   1.  Indicate that a candidate failed its HostageManifest validation because the prisoner did not have its captor set.
    
    # PARENT:
        *   NullException
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PRISONER_DOES_NOT_HAVE_CAPTOR_SET_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: Captor was not set."