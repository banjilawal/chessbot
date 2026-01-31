# src/chess/coord/database/core/exception/insertion/wrapper.py

"""
Module: chess.coord.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_COORD_INSERTION_FAILURE EXCEPTION #======================#
    "UniqueCoordInsertionFailedException",
]

from chess.coord import CoordException
from chess.system import InsertionFailedException


# ======================# UNIQUE_COORD_INSERTION_FAILURE EXCEPTION #======================#
class UniqueCoordInsertionFailedException(CoordException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique coord failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    # PARENT:
        *   CoordException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_COORD_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique coord insertion failed."