# src/chess/coordContext/builder/exception.py

"""
Module: ches.coordContext.builder.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import BuildException
from chess.coord import CoordContextException

___all__ = [
    # ======================# COORD_CONTEXT_BUILD_FAILURE #======================#
    "CoordContextBuildException",
]


# ======================# COORD_CONTEXT_BUILD_FAILURE #======================#
class CoordContextBuildException(CoordContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the CoordContext build creates an exception. Failed check exceptions are encapsulated
        in an CoordContextBuildException which is sent to the caller in a BuildResult.
    2.  The CoordContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   CoordContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "CoordContext build failed."