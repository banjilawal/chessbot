# src/chess/square/service/visitation/exception/start/add.py

"""
Module: chess.square.service.visitation.exception.start.add
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import InsertionException


__all__ = [
    # ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
    "StartingSquareVisitException",
]


# ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
class StartingSquareVisitException(SquareException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why adding an occupant to a square failed.

    # PARENT:
        *   SquareException
        *   InsertionException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_SQUARE_OCCUPANT_FAILURE"
    DEFAULT_MESSAGE = "Token entering a item failed."