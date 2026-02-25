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
    # ======================# TOKEN_CONTEXT_BUILD_FAILURE #======================#
    "TokenContextBuildException",
]


# ======================# TOKEN_CONTEXT_BUILD_FAILURE #======================#
class TokenContextBuildException(TokenContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token_context build operation failed. The exception chain
        traces the ultimate source of failure.

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
    ERR_CODE = "TOKEN_CONTEXT_BUILD_FAILED"
    MSG = "TokenContext build failed."