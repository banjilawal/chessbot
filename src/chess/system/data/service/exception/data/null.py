# src/chess/system/data/service/exception/data/null.py

"""
Module: chess.system.data.service.exception.data.null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DataException, DataServiceException, NullException

__all__ = [
    # ====================== REMOVING_NULL_DATA EXCEPTION #======================#
    "RemovingNullDataException",
]


# ====================== REMOVING_NULL_DATA EXCEPTION #======================#
class RemovingNullDataException(DataServiceException, DataException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate someone is trying to remove an item that does not exist in a collection.

    # PARENT:
        *   DataServiceException
        *   DataException
        *   NullException

    # PROVIDES:
    RemovingNullDataException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_NULL_DATA_ERROR"
    DEFAULT_MESSAGE = "Cannot remove data that does not exist in the set."