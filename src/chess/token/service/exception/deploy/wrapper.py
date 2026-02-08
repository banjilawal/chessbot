# src/chess/token/service/exception/deploy/wrapper.py

"""
Module: chess.token.service.exception.deploy.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_DEPLOYMENT_FAILURE EXCEPTION #======================#
    "TokenDeploymentFailedException",
]

from chess.token import TokenException
from chess.system import OperationFailedException

# ======================# TOKEN_DEPLOYMENT_FAILURE EXCEPTION #======================#
class TokenDeploymentFailedException(TokenException, OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a Token was not deployed onto its board. The exception chain traces
        the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "Token_DEPLOYMENT_FAILURE"
    DEFAULT_MESSAGE = "Token deployment failed."