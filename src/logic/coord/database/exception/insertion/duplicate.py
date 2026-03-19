# src/logic/coord/database/exception/duplicate.py

"""
Module: logic.coord.database.exception.duplicate
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from logic.coord import UniqueCoordStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_COORD EXCEPTION #======================#
    "AddingDuplicateCoordException",
]


# ======================# ADDING_DUPLICATE_COORD EXCEPTION #======================#
class AddingDuplicateCoordException(UniqueCoordStackException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a coord to the CoordDatabase's collider_candidates failed because the coord was
        already in the collection

    Super Class:
        *   CoordDatabaseException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_COORD_EXCEPTION"
    MSG = "Unique cord insertion failed."