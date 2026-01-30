# src/chess/coord/database/exception/duplicate.py

"""
Module: chess.coord.database.exception.duplicate
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import UniqueCoordDataServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_COORD EXCEPTION #======================#
    "AddingDuplicateCoordException",
]


# ======================# ADDING_DUPLICATE_COORD EXCEPTION #======================#
class AddingDuplicateCoordException(UniqueCoordDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a coord to the UniqueCoordDataService's dataset failed because the coord was
        already in the collection

    # PARENT:
        *   UniqueCoordDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_COORD_ERROR"
    DEFAULT_MESSAGE = "Unique cord insertion failed."