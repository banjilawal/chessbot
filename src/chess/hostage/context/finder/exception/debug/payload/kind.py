# src/chess/hostage/context/finder/exception/debug/payload/kind.py

"""
Module: chess.hostage.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import ResultException

_all__ = [
    # ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGES EXCEPTION #======================#
    "HostageSearchPayloadTypeException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGES EXCEPTION #======================#
class HostageSearchPayloadTypeException(HostageException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the HostageSearch ran successfully the payload was not a List[Hostage].
        This exception makes sure search payloads follow the convention of returning an array of matches not a
        single item.

    # PARENT:
        *   HostageException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGES_ERROR"
    MSG = "HostageSearch payload is the wrong type. The payload should be List[Hostage]."