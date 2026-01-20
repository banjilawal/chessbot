# src/chess/square/service/data/exception/insertion/full.py

"""
Module: chess.square.service.data.exception.insertion.full
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_SERVICE_CAPACITY EXCEPTION #======================#
    "SquareServiceCapacityException",
]

from chess.system import DebugException
from chess.square import SquareServiceException


# ======================# SQUARE_SERVICE_CAPACITY EXCEPTION #======================#
class SquareServiceCapacityException(SquareServiceException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a square to the service failed because the service has reached the limit of
        how many squares it manages. 

    # PARENT:
        *   DebugException
        *   SquareServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SERVICE_CAPACITY_ERROR"
    DEFAULT_MESSAGE = "Adding a square to the service failed: The number of squares managed is at full capacity."