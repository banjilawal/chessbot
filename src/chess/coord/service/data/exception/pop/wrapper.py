# src/chess/coord/service/data/exception/pop/wrapper.py

"""
Module: chess.coord.service.data.exception.pop.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_COORD_STACK_FAILURE EXCEPTION #======================#
    "PoppingCordStackFailedException",
]

from chess.coord import CoordDataServiceException
from chess.system import OperationFailedException


# ======================# POPPING_COORD_STACK_FAILURE EXCEPTION #======================#
class PoppingCordStackFailedException(CoordDataServiceException, OperationFailedException):
    """
    # ROLE: Exception Wrapper
    
    # RESPONSIBILITIES:
    1.  Encapsulate debug exceptions that indicate why a CoordStack pop fails. The encapsulated exceptions create
        chain for tracing the source of the failure.
    
    # PARENT:
        *   CoordDataServiceException
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_COORD_STACK_FAILURE"
    DEFAULT_MESSAGE = "Popping Coord Stack Failed."