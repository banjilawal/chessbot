# src/chess/square/service/exception/occupant/add/add.py

"""
Module: chess.square.service.exception.occupant.add.add
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import InsertionFailedException


__all__ = [
    # ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
    "AddingSquareOccupantFailedException",
]


# ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
class AddingSquareOccupantFailedException(SquareException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why adding an occupant to a square failed.

    # PARENT:
        *   SquareException
        *   InsertionFailedException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_SQUARE_OCCUPANT_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Token entering a item failed."