# src/chess/square/service/visitation/exception/terminate/empty.py

"""
Module: chess.square.service.visitation.exception.terminate.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# NO_VISIT_FOR_TERMINATION EXCEPTION #======================#
    "NoVisitForTerminationException",
]

from chess.square import SquareDebugException


# ======================# NO_VISIT_FOR_TERMINATION EXCEPTION #======================#
class NoVisitForTerminationException(SquareDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure DeletionResult was returned because there was no visitor in the square. There was no visit
    to terminate.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_VISIT_FOR_TERMINATION_ERROR"
    DEFAULT_MESSAGE = "Square visit termination failed: There was not visitor in the to eject."