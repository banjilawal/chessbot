# src/chess/hostage/builder/exception.py

"""
Module: chess.hostage.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import BuildException

__all__ = [
    # ======================# HOSTAGE_BUILD_FAILURE #======================#
    "HostageBuildException",
]


# ======================# HOSTAGE_BUILD_FAILURE #======================#
class HostageBuildException(HostageException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Hostage build creates an exception. Failed check exceptions are
        encapsulated in an HostageBuildException which is sent to the caller in a BuildResult.
    2.  The HostageBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   HostageException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_BUILD_FAILURE"
    DEFAULT_MESSAGE = "Hostage build failed."