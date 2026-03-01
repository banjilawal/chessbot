# src/logic/node/context/validator/exception/wrapper.py

"""
Module: logic.node.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.system import ValidationException
from logic.node import NodeContextException

__all__ = [
    # ======================# NODE_CONTEXT_VALIDATION_FAILURE #======================#
    "NodeContextValidationException",
]


# ======================# NODE_CONTEXT_VALIDATION_FAILURE #======================#
class NodeContextValidationException(NodeContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a NodeContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   NodeContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_CONTEXT_VALIDATION_FAILURE"
    MSG = "NodeContext validation failed."