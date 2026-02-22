# src/chess/coord/database/exception/deletion/wrapper.py

"""
Module: chess.coord.database.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EXHAUSTIVE_COORD_DELETION_FAILURE #======================#
    "ExhaustiveCoordDeletionException",
]

from chess.coord import CoordException
from chess.system import DeletionException


# ======================# EXHAUSTIVE_COORD_DELETION_FAILURE #======================#
class ExhaustiveCoordDeletionException(CoordException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why deleting all occurrences of a coord failed. deletion fails. The
        encapsulated exceptions create chain for tracing the source of the failure.

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
    ERROR_CODE = "EXHAUSTIVE_COORD_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Exhaustive coord deletion failed."