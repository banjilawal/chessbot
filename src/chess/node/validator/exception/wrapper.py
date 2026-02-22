# src/chess/node/validator/exception/wrapper.py

"""
Module: chess.node.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import ValidationException

__all__ = [
    # ======================# NODE_VALIDATION_FAILURE #======================#
    "NodeValidationException",
]


# ======================# NODE_VALIDATION_FAILURE #======================#
class NodeValidationException(NodeException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its Node validation.The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   NodeException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Node validation failed."