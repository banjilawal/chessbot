# src/chess/token/validator/exception/exception.py

"""
Module: chess.token.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import ContextException

__all__ = [
    # ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidTokenContextException",
]


# ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidTokenContextException(TokenContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a TokenContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidTokenContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidTokenContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   TokenContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TokenContext validation failed."