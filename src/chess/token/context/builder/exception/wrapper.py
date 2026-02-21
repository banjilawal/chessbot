# src/chess/token/_context/builder/exception/wrapper.py

"""
Module: chess.token.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BuildException
from chess.token import TokenContextException

__all__ = [
    # ======================# TOKEN_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "TokenContextBuildException",
]


# ======================# TOKEN_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class TokenContextBuildException(TokenContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the TokenContext build creates an exception. Failed check exceptions are encapsulated
        in an TokenContextBuildException which is sent to the caller in a BuildResult.
    2.  The TokenContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   TokenContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "TokenContext build failed."