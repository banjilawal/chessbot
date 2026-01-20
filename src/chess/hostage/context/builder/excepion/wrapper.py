# src/chess/hostage/context/builder/exception/wrapper.py

"""
Module: chess.hostage.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# CAPTIVITY_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "CaptivityContextBuildFailedException",
]

from chess.hostage import CaptivityContextException
from chess.system import BuildFailedException


# ======================# CAPTIVITY_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class CaptivityContextBuildFailedException(CaptivityContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the CaptivityContext build creates an exception. Failed check exceptions are encapsulated
        in an CaptivityContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The CaptivityContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   CaptivityContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CAPTIVITY_CONTEXT_BUILD_FAILURE"
    DEFAULT_MESSAGE = "CaptivityContext build failed."