# src/chess/attack/exception/wrapper.py

"""
Module: chess.attack.exception.wrapper
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACK_FAILURE #======================#
    "AttackFailedException",
]

from chess.attack import AttackException
from chess.system import OperationFailedException


# ======================# ATTACK_FAILURE #======================#
class AttackFailedException(AttackException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that were created when an attack is not completed successfully.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACK_FAILURE"
    DEFAULT_MESSAGE = "Attack failed."