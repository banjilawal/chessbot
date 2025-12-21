# src/chess/system/data/service/exception/null.py

"""
Module: chess.system.data.service.exception.null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DataServiceException, NullException

__all__ = [
    # ====================== REMOVING_NULL_DATA_SET EXCEPTION #======================#
    "RemovingNullDataSetException",
]


# ====================== REMOVING_NULL_DATA_SET EXCEPTION #======================#
class RemovingNullDataSetException(DataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate someone is trying to remove an item that does not exist in a collection.

    # PARENT:
        *   NullException
        *   DataServiceException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_NULL_DATA_ERROR"
    DEFAULT_MESSAGE = "Cannot remove data that does not exist in the set."