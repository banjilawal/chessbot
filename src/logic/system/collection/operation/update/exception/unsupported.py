# src/logic/system/collection/operation/update/exception/unsupported.py

"""
Module: logic.system.collection.operation.update.exception.unsupported
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyUpdateResultException",
]

from logic.system import MethodImplementationException


# ======================# UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyUpdateResultException(MethodImplementationException):
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
    ERR_CODE = "UNSUPPORTED_EMPTY_UPDATE_RESULT_STATE_EXCEPTION"
    MSG = (
        "An UpdateResult's outcome is either changed, change_failed, updated original == updated, failure."
        " It cannot be empty."
    )