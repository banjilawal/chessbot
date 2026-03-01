# src/logic/token/service/exception/deploy/wrapper.py

"""
Module: logic.token.service.exception.deploy.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_DEPLOYMENT_FAILURE #======================#
    "TokenDeploymentException",
]

from logic.token import TokenException
from logic.system import OperationException

# ======================# TOKEN_DEPLOYMENT_FAILURE #======================#
class TokenDeploymentException(TokenException, OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a Token was not deployed onto its token. The exception chain traces
        the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "Token_DEPLOYMENT_FAILURE"
    MSG = "Token deployment failed."