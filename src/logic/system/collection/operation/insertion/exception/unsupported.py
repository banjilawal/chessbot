# src/logic/system/collection/operation/insertion/exception/unsupported.py

"""
Module: logic.system.collection.operation.insertion.exception.unsupported
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyInsertionResultException",
]

from logic.system import MethodImplementationException


# ======================# UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyInsertionResultException(MethodImplementationException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that an InsertionResult can either succeed or fail. There are no other outcomes. 

    Super Class:
        *   UnsupportedDataResultStateException

    Provides:


    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE_EXCEPTION"
    MSG = "An InsertionResult's outcome is either success or failure. It cannot be empty."