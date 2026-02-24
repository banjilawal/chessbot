# src/chess/token/factory/exception

"""
Module: chess.token.factory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# TOKEN_BUILD_FAILURE #======================#
    "TokenBuildException",
]


# ======================# TOKEN_BUILD_FAILURE #======================#
class TokenBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in TokenBuilder.build that, prevented BuildResult.success() from 
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BUILD_FAILED"
    DEFAULT_MESSAGE = "Token build failed."