# src/logic/edge/context/validator/exception/debug/zero.py

"""
Module: logic.edge.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.edge import EdgeContextException

__all__ = [
    # ========================= ZERO_EDGE_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroEdgeContextFlagsException"
]


# ========================= ZERO_EDGE_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroEdgeContextFlagsException(EdgeContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a EdgeContext because none of its attributes was enabled.
        A single EdgeContext attribute.

    # PARENT:
        *   ContextFlagCountException
        *   EdgeContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ZERO_EDGE_CONTEXT_FLAGS_EXCEPTION"
    MSG = "EdgeContext validation failed: None of the flags were set. A single flag must be enabled."