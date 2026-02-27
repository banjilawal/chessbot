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
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in TokenVistHandler.terminate_visit that prevented a successful DeletionResult.

    # PARENT:
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_VISIT_TERMINATION_FAILURE"
    MSG = "Square visit termination failed."
    
    