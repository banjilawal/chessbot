# src/chess/system/data/operation/result/exception/unsupported.py

"""
Module: chess.system.data.operation.result.exception.unsupported
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_RESULT_RESULT_STATE EXCEPTION #======================#
    "UnsupportedDataResultStateException",
]

from chess.system import NotImplementedException


# ======================# UNSUPPORTED_EMPTY_RESULT_RESULT_STATE EXCEPTION #======================#
class UnsupportedDataResultStateException(NotImplementedException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that an ResultResult can either succeed or fail. There are no other outcomes.

    # PARENT:
        *   UnsupportedDataResultStateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "UNSUPPORTED_EMPTY_RESULT_RESULT_STATE_ERROR"
    DEFAULT_MESSAGE = "An ResultResult's outcome is either success or failure. It cannot be empty."