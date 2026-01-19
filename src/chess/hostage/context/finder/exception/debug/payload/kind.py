# src/chess/hostage/context/finder/exception/debug/payload/kind.py

"""
Module: chess.hostage.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.hostageManifest import HostageManifestException
from chess.system import ResultException

_all__ = [
    # ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGE_MANIFESTS EXCEPTION #======================#
    "HostageManifestSearchPayloadTypeException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGE_MANIFESTS EXCEPTION #======================#
class HostageManifestSearchPayloadTypeException(HostageManifestException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the HostageManifestSearch ran successfully the payload was not a List[HostageManifest].
        This exception makes sure search payloads follow the convention of returning an array of matches not a
        single item.

    # PARENT:
        *   HostageManifestException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_PAYLOAD_IS_NOT_LIST_OF_HOSTAGE_MANIFESTS_ERROR"
    DEFAULT_MESSAGE = "HostageManifestSearch payload is the wrong type. The payload should be List[HostageManifest]."