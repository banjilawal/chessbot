# src/chess/system/collection/exception/null.py

"""
Module: chess.system.collection.exception.null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


__all__ = [
    # ====================== NULL_COLLECTION EXCEPTION #======================#
    "NullCollectionException",
]

from chess.system import CollectionException, NullException


# ====================== NULL_COLLECTION EXCEPTION #======================#
class NullCollectionException(CollectionException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Team candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an TeamValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    3.  Catchall for errors not covered by lower level NullCollectionException subclasses.

    # PARENT:
     *   NullException
     *   CollectionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Collection cannot be null."