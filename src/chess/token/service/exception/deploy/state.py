# src/chess/token/service/exception/deploy/state.py

"""
Module: chess.token.service.exception.deploy.state
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_DEPLOYED_ON_BOARD EXCEPTION #======================#
    "TokenAlreadyDeployedOnBoardException",
]

from chess.token import TokenDebugException


# ======================# TOKEN_ALREADY_DEPLOYED_ON_BOARD EXCEPTION #======================#
class TokenAlreadyDeployedOnBoardException(TokenDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the attacker was targeting the wrong board,

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ALREADY_DEPLOYED_ON_BOARD"
    DEFAULT_MESSAGE = "Attack failed: The attacked is targeting the wrong board."