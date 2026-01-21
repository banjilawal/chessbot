# src/chess/system/data/collection/exception/null.py

"""
Module: chess.system.data.collection.exception.null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


__all__ = [
    # ====================== NULL_DATA_SET EXCEPTION #======================#
    "NullDatasetException",
]

from chess.system import DatasetException, NullException


# ====================== NULL_DATA_SET EXCEPTION #======================#
class NullDatasetException(DatasetException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Team candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an TeamValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
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