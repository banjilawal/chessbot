# src/chess/coord/service/data/exception/pop.py

"""
Module: chess.coord.service.data.exception.pop
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordDataServiceException

__all__ = [
    # ======================# POPPING_EMPTY_COORD_DATA_SERVICE EXCEPTION #======================#
    "PoppingEmtpyCoordDataServiceException",
]


# ======================# POPPING_EMPTY_COORD_DATA_SERVICE EXCEPTION #======================#
class PoppingEmtpyCoordDataServiceException(CoordDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a coord failed because the CoordDataService was not managing any coords.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_COORD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Coord deletion failed: CoordDataService does not own any coords."