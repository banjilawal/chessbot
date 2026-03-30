# src/logic/visit/exception/validator.py

"""
Module: logic.visit.exception.work
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# VISIT_FAILURE #======================#
    "VisitException",
]

from logic.system import OperationException


# ======================# VISIT_FAILURE #======================#
class VisitException(OperationException):
    """
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exceptions that were created when an visit is not completed successfully.

    Super Class:
        *   OperationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VISIT_FAILURE"
    MSG = "Visit failed."