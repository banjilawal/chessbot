# src/chess/square/service/visitation/exception/terminate/wrapper.py

"""
Module: chess.square.service.visitation.exception.terminate.wrapper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from chess.system import DeletionException

__all__ = [
    # ======================# SQUARE_VISIT_TERMINATION_FAILURE #======================#
    "SquareVisitTerminationException",
]


# ======================# SQUARE_VISIT_TERMINATION_FAILURE #======================#
class SquareVisitTerminationException(DeletionException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    Carry the Layer-1 DebugException which explains why the square visit was not terminated.

    # PARENT:
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_VISIT_TERMINATION_FAILURE"
    DEFAULT_MESSAGE = "Terminating the square visitation failed:."
    
    