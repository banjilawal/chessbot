# src/chess/visit/exception/wrapper.py

"""
Module: chess.visit.exception.wrapper
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# VISIT_FAILURE #======================#
    "VisitException",
]

from chess.system import OperationException


# ======================# VISIT_FAILURE #======================#
class VisitException(OperationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that were created when an visit is not completed successfully.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VISIT_FAILURE"
    MSG = "Visit failed."