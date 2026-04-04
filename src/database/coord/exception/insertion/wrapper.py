# src/logic/coord/database/kernel/exception/insertion/validator.py

"""
Module: logic.coord.database.kernel.exception.insertion.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_COORD_INSERTION_FAILURE #======================#
    "UniqueCoordInsertionException",
]

from logic.coord import CoordException
from system import InsertionException


# ======================# UNIQUE_COORD_INSERTION_FAILURE #======================#
class UniqueCoordInsertionException(CoordException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why inserting a unique coord failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    Super Class:
        *   CoordException
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNIQUE_COORD_INSERTION_FAILURE"
    MSG = "Unique coord insertion failed."