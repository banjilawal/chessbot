# src/chess/square/service/visitation/exception/terminate/wrapper.py

"""
Module: chess.square.service.visitation.exception.terminate.wrapper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import DeletionException

__all__ = [
    # ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
    "RemovingSquareOccupantException",
]


# ======================# REMOVING_SQUARE_OCCUPANT_FAILURE #======================#
class RemovingSquareOccupantException(DeletionException):
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