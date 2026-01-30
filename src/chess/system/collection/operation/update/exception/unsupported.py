# src/chess/system/collection/operation/update/exception/unsupported.py

"""
Module: chess.system.collection.operation.update.exception.unsupported
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyUpdateResultException",
]

from chess.system import UnsupportedDataResultStateException


# ======================# UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyUpdateResultException(UnsupportedDataResultStateException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that an UpdateResult can either succeed or fail. There are no other outcomes. 

    # PARENT:
        *   UnsupportedDataResultStateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE_ERROR"
    DEFAULT_MESSAGE = (
        "An UpdateResult's outcome is either changed, change_failed, current previous == current, failure."
        " It cannot be empty."
    )