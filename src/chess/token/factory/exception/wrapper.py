# src/chess/token/factory/exception

"""
Module: chess.token.factory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.token import TokenException
from chess.system import BuildFailedException

__all__ = [
    # ======================# TOKEN_BUILD_FAILURE EXCEPTION #======================#
    "TokenBuildFailedException",
]


# ======================# TOKEN_BUILD_FAILURE EXCEPTION #======================#
class TokenBuildFailedException(TokenException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Token build creates an exception. Failed check exceptions are encapsulated
        in an TokenBuildFailedException which is sent to the caller in a BuildResult.
    2.  The TokenBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   TokenException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BUILD_FAILED"
    DEFAULT_MESSAGE = "Token build failed."