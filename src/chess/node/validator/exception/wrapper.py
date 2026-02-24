# src/chess/node/validator/exception/wrapper.py

"""
Module: chess.node.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# NODE_VALIDATION_FAILURE #======================#
    "NodeValidationException",
]


# ======================# NODE_VALIDATION_FAILURE #======================#
class NodeValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in NodeValidator.validate that, prevented ValidationResult.success()
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Node validation failed."