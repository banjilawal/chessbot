# src/chess/system/err/implementation.py

"""
Module: chess.system.err.implementation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_DATA_RESULT_STATE EXCEPTION #======================#
    "UnsupportedDataResultStateException",
]

from chess.system import ChessException, NotImplementedException


# ======================# UNSUPPORTED_DATA_RESULT_STATE EXCEPTION #======================#
class UnsupportedDataResultStateException(NotImplementedException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that a Result class does not have logic for a DataResultState. Some data operations
        either succeed or fail. Others can have a null result.

    # PARENT:
        *   NotImplementedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "UNSUPPORTED_DATA_RESULT_STATE_ERROR"
    DEFAULT_MESSAGE = "DataResult does not support this outcome."