# src/chess/square/service/exception/occupant/add/add.py

"""
Module: chess.square.service.exception.occupant.add.add
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import DeletionFailedException

__all__ = [
    # ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
    "RemovingSquareOccupantFailedException",
]


# ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
class RemovingSquareOccupantFailedException(SquareException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why removing a token from a square failed..

    # PARENT:
        *   SquareException
        *   DeletionFailedException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_SQUARE_OCCUPANT_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Removing token from square failed."