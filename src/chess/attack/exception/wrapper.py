# src/chess/attack/exception/wrapper.py

"""
Module: chess.attack.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""



__all__ = [
    # ======================# ATTACK_FAILURE #======================#
    "AttackException",
]

from chess.system import OperationException


# ======================# ATTACK_FAILURE #======================#
class AttackException(OperationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in Attack.execute that, prevented AttackResult.success() 
        from being returned.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACK_FAILURE"
    DEFAULT_MESSAGE = "Attack attack failed."