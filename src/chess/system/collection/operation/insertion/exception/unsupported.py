# src/chess/system/collection/operation/insertion/exception/unsupported.py

"""
Module: chess.system.collection.operation.insertion.exception.unsupported
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyInsertionResultException",
]

from chess.system import UnsupportedDataResultStateException


# ======================# UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyInsertionResultException(UnsupportedDataResultStateException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that an InsertionResult can either succeed or fail. There are no other outcomes. 

    # PARENT:
        *   UnsupportedDataResultStateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "UNSUPPORTED_EMPTY_INSERTION_RESULT_STATE_ERROR"
    DEFAULT_MESSAGE = "An InsertionResult's outcome is either success or failure. It cannot be empty."