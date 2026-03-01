# src/logic/coord/context/finder/exception/dataset/null.py

"""
Module: logic.coord.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.coord import CoordException
from logic.system import NullDatasetException

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
    ERR_CODE = "COORD_DATASET_NULL_EXCEPTION"
    MSG = "Coord dataset cannot be null."