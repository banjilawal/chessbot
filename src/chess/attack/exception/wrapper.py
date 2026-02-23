# src/chess/attack/exception/wrapper.py

"""
Module: chess.attack.exception.wrapper
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACK_FAILURE #======================#
    "AttackException",
]

from chess.attack import AttackException
from chess.system import OperationException


# ======================# ATTACK_FAILURE #======================#
class AttackException(AttackException, OperationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that were created when an attack is not completed successfully.

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
    DEFAULT_MESSAGE = "Attack failed."