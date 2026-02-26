# src/chess/token/service/exception/deploy/state.py

"""
Module: chess.token.service.exception.deploy.state
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_DEPLOYED_ON_TOKEN EXCEPTION #======================#
    "TokenAlreadyDeployedOnTokenException",
]

from chess.token import TokenDebugException


# ======================# TOKEN_ALREADY_DEPLOYED_ON_TOKEN EXCEPTION #======================#
class TokenAlreadyDeployedOnTokenException(TokenDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the attacker was targeting the wrong token,

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_ALREADY_DEPLOYED_ON_TOKEN"
    MSG = "Attack failed: The attacked is targeting the wrong token."