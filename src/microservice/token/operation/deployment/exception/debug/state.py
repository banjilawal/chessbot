# src/logic/token/service/exception/deployment/state.py

"""
Module: logic.token.service.exception.deployment.state
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_DEPLOYED_ON_TOKEN EXCEPTION #======================#
    "TokenAlreadyDeployedOnTokenException",
]

from model.token import TokenDebugException


# ======================# TOKEN_ALREADY_DEPLOYED_ON_TOKEN EXCEPTION #======================#
class TokenAlreadyDeployedOnTokenException(TokenDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attack failed because the attacker was targeting the wrong token,

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_ALREADY_DEPLOYED_ON_TOKEN"
    MSG = "Attack failed: The attacked is targeting the wrong token."