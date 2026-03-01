# src/logic/hostage/context/finder/exception/dataset/null.py

"""
Module: logic.hostage.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.hostage import HostageException
from logic.system import NullDatasetException

_all__ = [
    # ======================# HOSTAGE__SEARCH_NULL_DATASET EXCEPTION #======================#
    "HostageSearchNullDatasetException",
]


# ======================# HOSTAGE__SEARCH_NULL_DATASET EXCEPTION #======================#
class HostageSearchNullDatasetException(HostageException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Hostage search operation failed because no dataset was provided for the query.

    # PARENT:
        *   HostageException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE__SEARCH_NULL_DATASET_EXCEPTION"
    MSG = "Hostage search failed: There was no dataset to search"