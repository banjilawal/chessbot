# src/chess/edge/context/builder/exception/wrapper.py

"""
Module: chess.edge.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import BuildException
from chess.edge import EdgeContextException


__all__ = [
    # ======================# EDGE_CONTEXT_BUILD_FAILURE #======================#
    "EdgeContextBuildException",
]


# ======================# EDGE_CONTEXT_BUILD_FAILURE #======================#
class EdgeContextBuildException(EdgeContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the EdgeContext build creates an exception. Failed check exceptions are encapsulated
        in an EdgeContextBuildException which is sent to the caller in a BuildResult.
    2.  The EdgeContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   EdgeContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "EdgeContext build failed."