# src/logic/coord/database/core/exception/stack/pop.py

"""
Module: logic.coord.database.core.exception.stack.pop
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_COORD_FROM_STACK_FAILURE #======================#
    "PoppingCoordStackFailedException",
]

from logic.coord import CoordException
from logic.system import DeletionException


# ======================# POPPING_COORD_FROM_STACK_FAILURE #======================#
class PoppingCoordStackFailedException(CoordException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why popping a Coord from the stack fails. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CoordException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_COORD_FROM_STACK_FAILURE"
    MSG = "Popping a coord from the stack failed."