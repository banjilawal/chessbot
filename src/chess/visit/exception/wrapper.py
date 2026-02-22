# src/chess/visit/exception/wrapper.py

"""
Module: chess.visit.exception.wrapper
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# VISIT_FAILURE #======================#
    "VisitFailedException",
]

from chess.system import OperationFailedException


# ======================# VISIT_FAILURE #======================#
class VisitFailedException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that were created when an visit is not completed successfully.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VISIT_FAILURE"
    DEFAULT_MESSAGE = "Visit failed."