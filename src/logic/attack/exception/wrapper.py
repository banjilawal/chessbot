# src/logic/attack/exception/wrapper.py

"""
Module: logic.attack.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""



__all__ = [
    # ======================# ATTACK_FAILURE #======================#
    "AttackException",
]

from logic.system import OperationException


# ======================# ATTACK_FAILURE #======================#
class AttackException(OperationException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERR_CODE = "ATTACK_FAILURE"
    MSG = "Attack attack failed."