# src/logic/arena/context/finder/exception/payload/kind.py

"""
Module: logic.arena.context.finder.exception.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.arena import ArenaException

_all__ = [
    # ======================# ARENA_DATASET_NULL EXCEPTION #======================#
    "ArenaDatasetNullException",
]


# ======================# ARENA_SEARCH_PAYLOAD_IS_NOT_LIST EXCEPTION #======================#
class ArenaSearchPayloadTypeException(ArenaException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the payload  of a successful ArenaSearch payload is not List[Arena].

    # PARENT:
        *   ArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_DATASET_NULL_EXCEPTION"
    MSG = "ArenaSearch payload is the wrong type. The payload should be List[Arena]."