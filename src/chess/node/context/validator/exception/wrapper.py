# src/chess/node/context/validator/exception/wrapper.py

"""
Module: chess.node.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.node import NodeContextException

__all__ = [
    # ======================# NODE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "NodeContextValidationFailedException",
]


# ======================# NODE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class NodeContextValidationFailedException(NodeContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a NodeContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   NodeContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "NodeContext validation failed."