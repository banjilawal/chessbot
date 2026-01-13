# src/chess/coord/service/data/exception/stack/pop.py

"""
Module: chess.coord.service.data.exception.stack.pop
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_COORD_FROM_STACK_FAILURE EXCEPTION #======================#
    "PoppingCoordStackFailedException",
]

from chess.coord import CoordException
from chess.system import DeletionFailedException


# ======================# POPPING_COORD_FROM_STACK_FAILURE EXCEPTION #======================#
class PoppingCoordStackFailedException(CoordException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why popping a Coord from the stack fails. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CoordException
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_COORD_FROM_STACK_FAILURE"
    DEFAULT_MESSAGE = "Popping a coord from the stack failed."