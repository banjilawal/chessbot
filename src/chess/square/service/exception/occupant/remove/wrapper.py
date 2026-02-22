# src/chess/square/service/exception/occupant/add/add.py

"""
Module: chess.square.service.exception.occupant.add.add
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import DeletionException

__all__ = [
    # ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
    "RemovingSquareOccupantException",
]


# ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
class RemovingSquareOccupantException(SquareException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why removing a occupant from a item failed..

    # PARENT:
        *   SquareException
        *   DeletionException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_SQUARE_OCCUPANT_FAILURE"
    DEFAULT_MESSAGE = "Removing occupant from item failed."