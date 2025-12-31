# src/chess/token/_context/builder/exception/wrapper.py

"""
Module: chess.token.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.token import TokenContextException

__all__ = [
    # ======================# TOKEN_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "TokenContextBuildFailedException",
]


# ======================# TOKEN_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class TokenContextBuildFailedException(TokenContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the TokenContext build creates an exception. Failed check exceptions are encapsulated
        in an TokenContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The TokenContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   TokenContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "TokenContext build failed."