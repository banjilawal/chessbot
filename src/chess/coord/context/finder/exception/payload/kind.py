# src/chess/coord/context/finder/exception/payload/kind.py

"""
Module: chess.coord.context.finder.exception.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordException


_all__ = [
    # ======================# COORD_DATASET_NULL EXCEPTION #======================#
    "CoordDatasetNullException",
]


# ======================# COORD_SEARCH_PAYLOAD_IS_NOT_LIST EXCEPTION #======================#
class CoordSearchPayloadTypeException(CoordException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the payload  of a successful CoordSearch payload is not List[Coord].

    # PARENT:
        *   CoordException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "CoordSearch payload is the wrong type. The payload should be List[Coord]."