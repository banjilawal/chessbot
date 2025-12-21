# src/chess/system/data/exception/null.py

"""
Module: chess.system.data.exception.null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DatasetException, NullException

__all__ = [
    # ====================== NULL_DATA_SET EXCEPTION #======================#
    "NullDatasetException",
]


# ====================== NULL_DATA_SET EXCEPTION #======================#
class NullDatasetException(DatasetException, NullException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions indicating an entity, method or operation requires a dataset but got null instead.
    3.  Catchall for errors not covered by lower level NullDatasetException subclasses.

    # PARENT:
     *   NullException
     *   DatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset cannot be null."