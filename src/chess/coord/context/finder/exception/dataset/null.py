# src/chess/coord/context/finder/exception/dataset/null.py

"""
Module: chess.coord.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import NullDatasetException

_all__ = [
    # ======================# COORD_DATASET_NULL EXCEPTION #======================#
    "CoordDatasetNullException",
]


# ======================# COORD_DATASET_NULL EXCEPTION #======================#
class CoordDatasetNullException(CoordException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that CoordContext validation failed because the candidate was null.

    # PARENT:
        *   CoordDatasetNullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "Coord dataset cannot be null."