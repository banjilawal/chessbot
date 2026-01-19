# src/chess/hostage/context/finder/exception/dataset/null.py

"""
Module: chess.hostage.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import NullDatasetException

_all__ = [
    # ======================# HOSTAGE_MANIFEST__SEARCH_NULL_DATASET EXCEPTION #======================#
    "HostageManifestSearchNullDatasetException",
]


# ======================# HOSTAGE_MANIFEST__SEARCH_NULL_DATASET EXCEPTION #======================#
class HostageManifestSearchNullDatasetException(HostageManifestException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a HostageManifest search operation failed because no dataset was provided for the query.

    # PARENT:
        *   HostageManifestException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST__SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "HostageManifest search failed: There was no dataset to search"