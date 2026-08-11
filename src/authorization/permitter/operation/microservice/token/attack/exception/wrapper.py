# src/logic/attack/exception/validator.py

"""
Module: logic.attack.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""



__all__ = [
    # ======================# ATTACK_FAILURE #======================#
    "AttackException",
]

from system import OperationException


# ======================# ATTACK_FAILURE #======================#
class AttackException(OperationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  An error occurred in Attack.execute that, prevented AttackResult.success() 
        from being returned.

    Super Class:
        *   TransactionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACK_FAILURE"
    MSG = "Attack attack failed."