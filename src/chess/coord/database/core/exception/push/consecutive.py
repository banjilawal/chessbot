# src/chess/coord/database/core/exception/stack/consecutive.py

"""
Module: chess.coord.database.core.exception.stack.consecutive
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

# ======================# MAX_CONSECUTIVE_COORD_POP EXCEPTION #======================#
from chess.coord import CoordDataServiceException


class MaxConsecutiveCoordPopException(CoordDataServiceException):
        """
        # ROLE: Debug, Error Tracing
    
        # RESPONSIBILITIES:
        1.  Indicate that a CoordStack pop failed because the had not been a different coord pushed since the
            last pop.
    
        # PARENT:
            *   CoordStackException
    
        # PROVIDES:
        None
    
        # LOCAL ATTRIBUTES:
        None
    
        # INHERITED ATTRIBUTES:
        None
        """
        ERROR_CODE = "MAX_CONSECUTIVE_COORD_POP_ERROR"
        DEFAULT_MESSAGE = "Popping Coord Stack Failed: Two pops cannot be made in a row. A pop must follow a push."