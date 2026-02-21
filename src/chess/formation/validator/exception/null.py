# src/chess/formation/validator/exception/name.py

"""
Module: chess.formation.validator.exception.name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import FormationValidationException

__all__ = [
    # ======================# NULL_FORMATION EXCEPTION #======================#
    "NullFormationException",
]


# ======================# NULL_FORMATION EXCEPTION #======================#
class NullFormationException(FormationValidationException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Formation validation candidate is null.
    2.  Raised if an entity, method or operation requires an Formation but receives null instead.

    # PARENT:
        *   FormationValidationException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ORDER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "Formation cannot be null."