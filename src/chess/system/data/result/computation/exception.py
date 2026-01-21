# src/chess/system/data/result/computation/exception.py

"""
Module: chess.system.data.result.computation.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_COMPUTATION_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyComputationResultException",
]

from chess.system import UnsupportedDataResultStateException


# ======================# UNSUPPORTED_EMPTY_COMPUTATION_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyComputationResultException(UnsupportedDataResultStateException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that an ComputationResult can either succeed or fail. There are no other outcomes. 

    # PARENT:
        *   UnsupportedDataResultStateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "UNSUPPORTED_EMPTY_COMPUTATION_RESULT_STATE_ERROR"
    DEFAULT_MESSAGE = "An ComputationResult's outcome is either success or failure. It cannot be empty."