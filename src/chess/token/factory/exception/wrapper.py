# src/chess/token/factory/exception

"""
Module: chess.token.factory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.token import TokenException
from chess.system import BuildException

__all__ = [
    # ======================# TOKEN_BUILD_FAILURE#======================#
    "TokenBuildException",
]


# ======================# TOKEN_BUILD_FAILURE #======================#
class TokenBuildException(TokenException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token build operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BUILD_FAILURE"
    DEFAULT_MESSAGE = "Token build failed."