# src/logic/system/collection/operation/search/query/service/exception/super.py

"""
Module: logic.system.collection.operation.search.query.service.exceptionsuper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from logic.system import ChessException

__all__ = [
    # ======================# CONTEXT EXCEPTION #======================#
    "ContextException",
]


# ======================# CONTEXT EXCEPTION #======================#
class ContextException(ChessException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Parent of exception raised by CONTEXT objects
    3.  Super for CONTEXT errors not covered by lower level CONTEXT exception.

    Super Class:
        *   ChessException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CONTEXT_EXCEPTION"
    MSG = "CONTEXT raised an exception."
