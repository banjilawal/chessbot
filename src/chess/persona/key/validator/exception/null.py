# src/chess/persona/key/validator/exception/null.py

"""
Module: chess.persona.key.validator.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from chess.system import NullException
from chess.persona import InvalidPersonaSuperKeyException

__all__ = [
    # ======================# NULL_PERSONA_SUPER_KEY EXCEPTION #======================#
    "NullPersonaSuperKeyException",
]


# ======================# NULL_PERSONA_SUPER_KEY EXCEPTION #======================#
class NullPersonaSuperKeyException(InvalidPersonaSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an PersonaSuperKey validation candidate is null.
    2.  Raised if an entity, method or operation requires an PersonaSuperKey but receives null instead.

    # PARENT:
        *   InvalidPersonaSuperKeyException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PERSONA_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "PersonaSuperKey cannot be null."