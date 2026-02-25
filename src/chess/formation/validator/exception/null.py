# src/chess/formation/validator/exception/null.py

"""
Module: chess.formation.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_FORMATION EXCEPTION #======================#
    "NullFormationException",
]

from chess.system import NullException
from chess.formation import FormationDebugException


# ======================# NULL_FORMATION EXCEPTION #======================#
class NullFormationException(FormationDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   FormationDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_FORMATION_ERROR"
    DEFAULT_MESSAGE = "Formation validation failed: The candidate cannot be null."